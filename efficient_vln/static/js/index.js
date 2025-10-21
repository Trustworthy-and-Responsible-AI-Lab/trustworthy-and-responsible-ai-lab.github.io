window.HELP_IMPROVE_VIDEOJS = false;


$(document).ready(function() {
    // Check for click events on the navbar burger icon

    var options = {
			slidesToScroll: 1,
			slidesToShow: 1,
			loop: true,
			infinite: true,
			autoplay: true,
			autoplaySpeed: 5000,
    }

		// Initialize all div with carousel class
    var carousels = bulmaCarousel.attach('.carousel', options);
	
    bulmaSlider.attach();

})

document.addEventListener("DOMContentLoaded", function () {
	(function () {
		const root = document.getElementById('results-carousel');
		const slides = Array.from(root.querySelectorAll('.item'));
		const prevBtn = root.querySelector('.carousel-btn.prev');
		const nextBtn = root.querySelector('.carousel-btn.next');
		// const captionEl = document.getElementById('carousel-caption'); // 👈 new line


		let idx = 0;
		const intervalMs = 5000;     // auto-advance every 3s
		let timer = null;
		let paused = false;

		function show(i) {
			slides.forEach((el, j) => el.classList.toggle('active', j === i));
			// Update ARIA labelling (1-based)
			slides.forEach((el, j) => el.setAttribute('aria-label', `${j + 1} of ${slides.length}`));

			// 👇 NEW: update caption text dynamically
			// if (captionEl) {
			// const text = slides[i].dataset.caption || '';
			// captionEl.textContent = text;
			// }
		}

		function next() { idx = (idx + 1) % slides.length; show(idx); }
		function prev() { idx = (idx - 1 + slides.length) % slides.length; show(idx); }

		function start() {
			stop();
			timer = setInterval(next, intervalMs);
		}
		function stop() {
			if (timer) { clearInterval(timer); timer = null; }
		}

		// Initial
		show(0);
		start();

		// Click anywhere on the carousel (except the arrows) toggles pause/resume
		root.addEventListener('click', (e) => {
			if (e.target.closest('.carousel-btn')) return; // ignore arrow clicks here
			paused = !paused;
			paused ? stop() : start();
		});

		// Arrow buttons also pause autoplay on user interaction
		prevBtn.addEventListener('click', (e) => { e.stopPropagation(); paused = true; stop(); prev(); });
		nextBtn.addEventListener('click', (e) => { e.stopPropagation(); paused = true; stop(); next(); });

		// Keyboard support when the carousel is focused
		root.tabIndex = 0; // make focusable
		root.addEventListener('keydown', (e) => {
			if (e.key === 'ArrowLeft') { paused = true; stop(); prev(); }
			if (e.key === 'ArrowRight') { paused = true; stop(); next(); }
			if (e.key.toLowerCase() === ' ') { // space toggles play/pause
			e.preventDefault();
			paused = !paused;
			paused ? stop() : start();
			}
		});

	// Optional: pause while hovering; resume when leaving if not explicitly paused via click
	// root.addEventListener('mouseenter', () => !paused && stop());
	// root.addEventListener('mouseleave', () => !paused && start());
	})();
});

