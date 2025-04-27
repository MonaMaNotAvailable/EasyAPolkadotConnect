module.exports = {
    content: [
      "./src/**/*.{html,js,jsx,ts,tsx}",  // Ensure Tailwind CSS processes all your relevant files
    ],
    theme: {
      extend: {
        colors: {
          primary: '#0070f3',   // Add custom primary color if needed
          secondary: '#f2f2f2',  // Add secondary colors
        },
        spacing: {
          '128': '32rem',  // Custom spacing sizes
          '144': '36rem',
        },
        fontFamily: {
          sans: ['Inter', 'Arial', 'sans-serif'],  // Custom font family
        },
        boxShadow: {
          'card': '0 4px 6px rgba(0, 0, 0, 0.1)', // Custom shadow for cards
        },
      },
    },
    plugins: [
      // Any additional plugins you might need can be added here.
    ],
    // Purge unused styles in production for better performance
    purge: {
      enabled: true,
      content: ['./src/**/*.{html,js,jsx,ts,tsx}'],
    },
  }
  