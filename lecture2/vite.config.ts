import MarkdownItMark from 'markdown-it-mark'
import { defineConfig } from 'vite'

export default defineConfig({
  slidev: {
    markdown: {
      async markdownSetup(md) {
        md.use(MarkdownItMark)
      },
    },
  },
})
