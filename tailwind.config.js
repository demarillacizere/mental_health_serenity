import colors from "tailwindcss/colors"
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
	content: [
		'./templates/**/*.html'
	],
	theme: {
    extend: {
      colors:{
        secondary:{
          DEFAULT: colors.neutral[200],
          hover: colors.neutral[300],
          border: colors.neutral[400],
          text: colors.neutral[500],
          dark: colors.neutral[800],
          ["dark-hover"]: colors.neutral[900],
        },
        primary:{
          ["gradient-start"]:'#5EB47C',
          ["gradient-end"]:'#007D6E',
          green: '#EC744A',
          orange: '#ec744a',
        }
      }
    },
  },
	plugins: [],

}


