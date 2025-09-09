module.exports = function (config) {
  config.set({
    // ... autres configs
    browsers: ['Chrome', 'ChromeHeadless'],
    customLaunchers: {
      ChromeHeadless: {
        base: 'Chrome',
        flags: [
          '--headless',
          '--disable-gpu',
          '--no-sandbox',
          '--disable-dev-shm-usage'
        ]
      }
    }
  });
};