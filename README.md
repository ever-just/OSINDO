# Osindo Mechanical Services

Landing page for Osindo Mechanical Services (HVAC, auto, and mechanical repair in the Twin Cities).

## Tech Stack
- Static HTML/CSS/JS (no build step)
- Netlify hosting & CI/CD (`netlify deploy`)
- GoDaddy DNS via simple Python helper scripts in `scripts/`

## Getting Started
```bash
# Serve locally (e.g., with python http.server)
python3 -m http.server 8080
```

## Deployment
Deployments are handled through Netlify CLI.
```bash
netlify deploy --prod --dir=.
```
Ensure `netlify login` has been run and the folder is linked to the `osindo-mechanical-services` project.

## DNS Management
`scripts/update_dns.py` uses the shared GoDaddy SDK (in `~/Documents/GoDaddySDK`) to point `osindo.us` to the Netlify site. Set `GODADDY_*` env variables before running.

## Customer Portal
Primary CTA drives to the Assembly portal:
```
https://osindosmechanicalservices.myassembly.com/login?step=signUp
```

## Assets
- Favicon: `assets/favicon.png`
- Hero media uses Unsplash placeholder (replace with branded imagery when available).

## Legal
Privacy Policy and Terms & Conditions content is embedded near the footer. Update as official documents evolve.
