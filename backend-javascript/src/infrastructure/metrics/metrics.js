import client from 'prom-client';

const PROMETHEUS_ENABLED = process.env.PROMETHEUS_ENABLED === 'true';

if (PROMETHEUS_ENABLED) {
  client.collectDefaultMetrics();
}

let httpRequestCounter = null;

if (PROMETHEUS_ENABLED) {
  httpRequestCounter = new client.Counter({
    name: 'http_requests_total',
    help: 'Nombre total de requêtes HTTP',
    labelNames: ['method', 'route', 'status'],
  });
}

function incrementHttpRequests(method, route, status) {
  if (httpRequestCounter) {
    httpRequestCounter.inc({
      method: method,
      route: route,
      status: String(status),
    });
  }
}

export { client, incrementHttpRequests };
