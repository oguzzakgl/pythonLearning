/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                // Custom color palette based on "Cyber-Chic" prompt
                dark: {
                    DEFAULT: '#0a0a0a',
                    to: '#1a0b2e' // deeper purple
                },
                primary: {
                    DEFAULT: '#7c3aed', // Electric Violet
                    glow: '#a855f7'     // Neon Purple
                }
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
            }
        },
    },
    plugins: [],
}
