/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./budgetapp/**/*.{html,js}'],
    darkMode: 'class',
    theme: {
        extend: {
            container: {
                center: true,
            },
            colors: {
                'primary': '#FCBE5B',
                'secondary': '#F5604A',
                'third': '#7EB67E',
                'dark': '#202020'
            },
            fontFamily: {
                poppins: ['Poppins', 'sans-serif']
            }
        },
    },
    plugins: [],
}
