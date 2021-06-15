function toggleTheme() {
            var theme = document.getElementsByTagName('link')[0];
            if (theme.getAttribute('href') == 'register_style.css') {
                theme.setAttribute('href', 'register_style_dark.css');
            } else {
                theme.setAttribute('href', 'register_style.css');
            }
        }