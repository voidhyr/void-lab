# Docker Fundamentals

**Date:** 2026-06-27
**Goal:** Build real Docker fundamentals from scratch — Dockerfile, networking, Compose

## Session 1

### Environment
- Docker 29.6.1
- Docker Compose v5.2.0
- OS: Ubuntu (ProBook)

### Plan
- [x] Write first Dockerfile (Python script)
- [x] Build and run image, understand layers
- [x] Docker networking basics
- [x] Docker Compose — multi-container setup
- [x] Volumes — persistent data

### Notes
### What I did

- Wrote first Dockerfile from scratch
- Fixed WORKDIR (host path → /usr/local/app)
- Fixed COPY (script.py → .)
- Built image: `docker build -t sys-info .`
- Ran from a different directory — worked fine, image is stored in Docker not filesystem

### Key observations

**Container OS vs host OS**
- Output showed Linux 7.0.0-27-generic, not Ubuntu
- Container runs its own isolated OS layer
- `platform.system()` returns the container's OS, not the host

**Image layers (`docker image history sys-info`)**
- Every Dockerfile instruction = one layer
- Top 3 layers = mine (CMD, COPY, WORKDIR) — tiny, created minutes ago
- All layers below = inherited from python:3.14 base (~1GB, Debian + Python)
- Layers are cached — unchanged layers don't rebuild
- Instruction order matters: put stable things at top, changing things at bottom
- COPY is correctly at the bottom (changes most often)

### Docker Networking

**Default networks**
- bridge — default, containers isolated from host but can talk to each other
- host — container shares host network directly, no isolation
- none — no networking

**Bridge network**
- Subnet: 172.17.0.0/16, Gateway: 172.17.0.1
- Virtual interface: docker0 on host
- Containers get IPs automatically starting from 172.17.0.2

**Experiment**
- Ran nginx as webserver: got 172.17.0.2
- Ran alpine container, pinged 172.17.0.2 → 0% packet loss
- Two containers communicating over bridge network
- sys-info container showed empty in bridge inspect — exits immediately, no long-running process

**Key insight**
- Same concept as physical/virtual networking — just docker-managed
- Containers on same bridge can reach each other by IP
- Isolated from host by default

### Docker Compose

**What it is**
- Define and run multiple containers with a single file
- No need to install services locally — Docker pulls images automatically

**docker-compose.yml structure**
- `services:` — define each container
- `build: .` — build from local Dockerfile
- `image:` — pull from Docker Hub

**Experiment**
- Two services: app (Python script) + redis (redis:alpine)
- app ran script.py and exited cleanly (code 0)
- redis stayed running on port 6379/tcp
- `docker compose ps` shows status of each service

**Fix applied**
- Removed `version: "3.8"` — obsolete in modern Compose, causes warning

**Key commands**
- `docker compose up` — start all services
- `docker compose down` — stop and remove containers
- `docker compose ps` — check status
