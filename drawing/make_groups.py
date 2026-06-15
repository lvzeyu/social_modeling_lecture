#!/usr/bin/env python3
import argparse
import csv
import random
from pathlib import Path


DEFAULT_INPUT = Path(__file__).with_name("names.csv")
DEFAULT_OUTPUT = Path(__file__).with_name("groups.csv")
GROUP_SIZE = 4
ROUNDS = ("1", "2")


def read_members(path):
    with path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        required = {"name", "fixed_round", "fixed_group"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Missing columns in {path}: {', '.join(sorted(missing))}")

        members = []
        seen = set()
        for line_number, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            if not name:
                continue
            if name in seen:
                raise SystemExit(f"Duplicate name at line {line_number}: {name}")
            seen.add(name)

            fixed_round = (row.get("fixed_round") or "").strip()
            fixed_group = (row.get("fixed_group") or "").strip()
            if fixed_round and fixed_round not in ROUNDS:
                raise SystemExit(
                    f"Invalid fixed_round at line {line_number}: {fixed_round} "
                    f"(use 1, 2, or leave blank)"
                )

            members.append(
                {
                    "name": name,
                    "fixed_round": fixed_round,
                    "fixed_group": fixed_group,
                }
            )
    return members


def group_fixed_members(members):
    fixed_groups = {}
    free_members = []

    for member in members:
        fixed_group = member["fixed_group"]
        if fixed_group:
            fixed_groups.setdefault(fixed_group, []).append(member)
        else:
            free_members.append(member)

    groups = []
    for fixed_group, group_members in sorted(fixed_groups.items()):
        if len(group_members) > GROUP_SIZE:
            raise SystemExit(
                f"Fixed group {fixed_group} has {len(group_members)} people; "
                f"maximum is {GROUP_SIZE}."
            )
        groups.append(
            {
                "fixed_group": fixed_group,
                "members": group_members,
            }
        )

    return groups, free_members


def add_free_members(groups, free_members, rng):
    rng.shuffle(free_members)

    for group in groups:
        while free_members and len(group["members"]) < GROUP_SIZE:
            group["members"].append(free_members.pop())

    while free_members:
        groups.append(
            {
                "fixed_group": "",
                "members": free_members[:GROUP_SIZE],
            }
        )
        del free_members[:GROUP_SIZE]

    # If the last group is too small, move people from earlier full non-fixed groups
    # so the result prefers 3-person groups over 1- or 2-person groups.
    if len(groups) >= 2 and len(groups[-1]["members"]) < 3:
        last_group = groups[-1]
        for group in groups[:-1]:
            if group["fixed_group"]:
                continue
            if len(group["members"]) > 3:
                last_group["members"].append(group["members"].pop())
            if len(last_group["members"]) == 3:
                break

    return groups


def choose_round(group, fallback_round):
    fixed_rounds = {member["fixed_round"] for member in group["members"] if member["fixed_round"]}
    if len(fixed_rounds) > 1:
        names = ", ".join(member["name"] for member in group["members"])
        raise SystemExit(f"Conflicting fixed_round values in group with: {names}")
    if fixed_rounds:
        return fixed_rounds.pop()
    return fallback_round


def write_groups(groups, output_path):
    rows = []
    for index, group in enumerate(groups, start=1):
        fallback_round = ROUNDS[(index - 1) % len(ROUNDS)]
        presentation_round = choose_round(group, fallback_round)
        group_name = group["fixed_group"] or f"G{index:02d}"
        for member in group["members"]:
            rows.append(
                {
                    "group": group_name,
                    "presentation_round": presentation_round,
                    "name": member["name"],
                    "fixed_round": member["fixed_round"],
                    "fixed_group": member["fixed_group"],
                }
            )

    with output_path.open("w", newline="", encoding="utf-8") as file:
        fieldnames = ["group", "presentation_round", "name", "fixed_round", "fixed_group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return rows


def main():
    parser = argparse.ArgumentParser(description="Split names into groups of 4.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Input CSV path.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output CSV path.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible groups.")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    members = read_members(args.input)
    fixed_groups, free_members = group_fixed_members(members)
    groups = add_free_members(fixed_groups, free_members, rng)
    rows = write_groups(groups, args.output)

    group_count = len({row["group"] for row in rows})
    print(f"Wrote {len(rows)} people into {group_count} groups: {args.output}")


if __name__ == "__main__":
    main()
