import { ApplicationConfig, isDevMode, LOCALE_ID, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter, withInMemoryScrolling } from '@angular/router';
import { provideClientHydration } from '@angular/platform-browser';
import { provideServiceWorker } from '@angular/service-worker';

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    {
      provide: LOCALE_ID,
      useValue: 'fr',
    },

    provideHttpClient(),

    provideBrowserGlobalErrorListeners(),

    provideRouter(
      routes,
      withInMemoryScrolling({
        scrollPositionRestoration: 'enabled',
        anchorScrolling: 'enabled',
      }),
    ),

    provideClientHydration(),

    provideServiceWorker('ngsw-worker.js', {
      enabled: !isDevMode(),
      registrationStrategy: 'registerWhenStable:30000',
    }),
  ],
};

// import { ApplicationConfig, LOCALE_ID, isDevMode, provideBrowserGlobalErrorListeners } from '@angular/core';
// import { provideHttpClient, withFetch } from '@angular/common/http';
// import { provideRouter, withInMemoryScrolling } from '@angular/router';
// import { provideClientHydration } from '@angular/platform-browser';
// import { provideServiceWorker } from '@angular/service-worker';

// import { routes } from './app.routes';

// export const appConfig: ApplicationConfig = {
//   providers: [
//     { provide: LOCALE_ID, useValue: 'fr' },

//     provideHttpClient(
//       withFetch(),
//     ),

//     provideBrowserGlobalErrorListeners(),

//     provideRouter(
//       routes,
//       withInMemoryScrolling({
//         scrollPositionRestoration: 'enabled',
//         anchorScrolling: 'enabled',
//       }),
//     ),

//     provideClientHydration(),

//     provideServiceWorker('ngsw-worker.js', {
//       enabled: !isDevMode(),
//       registrationStrategy: 'registerWhenStable:30000',
//     }),
//   ],
// };


// import { ApplicationConfig, provideBrowserGlobalErrorListeners, isDevMode } from '@angular/core';
// import { provideRouter } from '@angular/router';

// import { routes } from './app.routes';
// import { provideClientHydration } from '@angular/platform-browser';
// import { provideServiceWorker } from '@angular/service-worker';
// import { withInMemoryScrolling } from '@angular/router';

// import { provideHttpClient, withFetch } from '@angular/common/http';

// export const appConfig: ApplicationConfig = {
//   providers: [
//     provideHttpClient(
//       withFetch(),
//     ),
//     provideBrowserGlobalErrorListeners(),
//     provideRouter(routes,
//       withInMemoryScrolling({
//         scrollPositionRestoration: 'enabled',
//         anchorScrolling: 'enabled',
//       }),
//     ),
//     provideClientHydration(),
//     provideServiceWorker('ngsw-worker.js', {
//       enabled: !isDevMode(),
//       registrationStrategy: 'registerWhenStable:30000',
//     }),
//   ],
// };
