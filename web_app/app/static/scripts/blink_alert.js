            // Toggles visibility of greeting
            function blink() {
                let body = document.querySelector('a');
                if (!body.classList.contains('hovered')) {
                    if (body.style.visibility == 'hidden') {
                        body.style.visibility = 'visible';
                    } else {
                        body.style.visibility = 'hidden';
                    }
                }
            }

            // Add event listeners for mouseover and mouseout
            let link = document.querySelector('a');
            link.addEventListener('mouseover', function() {
                link.classList.add('hovered');
            });

            link.addEventListener('mouseout', function() {
                link.classList.remove('hovered');
            });

            // Blink every 500ms
            window.setInterval(blink, 500);
        