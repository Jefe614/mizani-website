### Mizani Site

Provides a shared Mizani Labs homepage at `/` and branded Frappe login styling
for tenant sites. Tenant-specific logos configured in Website Settings take
precedence over the bundled fallback logo.

### Installation

From the bench directory, install the app on all sites:

```bash
bench --site all install-app mizani_site
bench build --app mizani_site
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/mizani_site
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
