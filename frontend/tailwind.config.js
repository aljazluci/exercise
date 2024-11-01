/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "color-orange-on-dark": "var(--color-orange-on-dark)",
        "color-dark": "var(--color-dark)"
      }
    },
  },
  plugins: [],
}

