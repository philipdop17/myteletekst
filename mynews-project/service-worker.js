const CACHE_NAME = 'mynews-v1';
const urlsToCache = [
  './mynews.html',
  // Add your CSS/JS if separated, or external libs if any
  // e.g. './styles.css', './script.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});