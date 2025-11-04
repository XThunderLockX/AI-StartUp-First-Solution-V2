/**** Tailwind CSS configuration for the Retail AI frontend ****/
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#2563eb',
          dark: '#1e40af',
        },
      },
    },
  },
  plugins: [],
}
