<script setup>
import { renderSVG } from 'uqr'
import { computed } from 'vue'

const props = defineProps({
  value: { type: String, required: true },
  width: { type: Number, default: 160 },
  height: { type: Number, default: 160 },
})

const svg = computed(() => renderSVG(props.value))
</script>

<template>
  <div :style="{ width: width + 'px', height: height + 'px' }" v-html="svg" />
</template>
