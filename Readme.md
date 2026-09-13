# void-lab

> A hands-on software development lab for learning, building, and independent experiments.
> Exploring the Void — From Curiosity to Creation.

## About

I'm Dani (voidhyr), an aspiring Software Engineer interested in building useful
software and understanding how systems work. This repository documents my
practice with Python, SQL, software development, and data systems.

My broader interests include AI models, security, Linux, and independent,
non-academic research. Data engineering is one area I’m exploring, rather than
the only direction of this lab. Work here may support personal or college
projects; each project should explain its purpose and current status.

## Learning Order

This is a learning roadmap, not a list of completed skills. Use Git, the Linux
terminal, and debugging throughout; practise SQL alongside Python once the
Python basics are comfortable.

| Order | Focus                                                                                                  | Practical milestone                                                                                 | Location                          |
| ----- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | --------------------------------- |
| 1     | Python foundations: collections, functions, files, exceptions, modules, and classes                    | Build a small command-line tool and explain its behavior                                            | `fundamentals/` — existing        |
| 2     | Software development: project structure, virtual environments, dependencies, Git, debugging, and tests | Turn a script into a documented project with meaningful pytest tests                                | `software-development/` — planned |
| 3     | SQL and PostgreSQL: joins, aggregation, schemas, constraints, transactions, and indexes                | Build a Python tool that stores and queries data                                                    | `sql/` — planned                  |
| 4     | HTTP and FastAPI: requests, responses, validation, and error handling                                  | Expose a database-backed feature through an API                                                     | `backend/` — planned              |
| 5     | Docker and development automation                                                                      | Run the application and PostgreSQL with Docker Compose; automate tests                              | `environments/` — planned         |
| 6     | Data processing, modeling, and pipelines                                                               | Build ingestion, transformation, validation, and safe reruns; add Airflow when scheduling is needed | `data/` — planned                 |
| 7     | AI and research experiments                                                                            | Ask a specific question, establish a baseline, and record reproducible results                      | `experiments/` — planned          |

Study basic data structures and algorithms alongside these projects. Advanced
algorithm exercises do not need to block building useful software.

## Existing Structure

| Folder                         | Contents                                                            |
| ------------------------------ | ------------------------------------------------------------------- |
| `fundamentals/basics/`         | Introductory Python exercises and small scripts                     |
| `fundamentals/intermediate/`   | Additional Python practice and small games                          |
| `fundamentals/intermediate-2/` | Collections, loops, and other practice scripts                      |
| `fundamentals/oop/`            | Object-oriented programming practice                                |
| `fundamentals/patterns/`       | Pattern-printing exercises                                          |
| `fundamentals/dsa/`            | Searching, sorting, graph algorithms, and other exercises           |
| `archive/`                     | Earlier DevOps, networking, and project work retained for reference |

Planned folders in the roadmap will be added when they contain actual work.

## Current Project: Weather ETL Pipeline

My college ETL project is an opportunity to practise Python, SQL, and reliable
data processing. The intended workflow collects weather data from the
OpenWeatherMap API, validates records, loads a PostgreSQL star schema, and
schedules processing with Apache Airflow. Looker Studio is the planned
reporting layer; its connection to local data needs to be handled separately.

Project repository: [proETL](https://github.com/voidhyr/proETL)

Implementation status belongs in the project README. Future extensions should
follow a concrete need or experiment rather than a checklist of tools.

## Tools and Direction

- **Foundation:** Python, SQL, Git, and Linux
- **Development roadmap:** PostgreSQL, pytest, FastAPI, and Docker
- **Data project tools:** pandas and Apache Airflow
- **Future exploration:** AI models, security, and Linux experiments

## Working Principles

- Build small, working programs before expanding their scope.
- Understand code well enough to explain, change, and debug it.
- Use AI as a learning aid; verify generated code and document assistance where relevant.
- Write tests for meaningful behavior, including failure cases.
- Document each project’s purpose, setup, limitations, and lessons learned.
- Run experiments in a controlled environment and record results honestly.

## Connect

[**Enter the Void → Personal Site**](https://voidhyr.github.io/Personal-Website/)

[Articles](https://dev.to/voidhyr) · [X](https://x.com/voidhyr)

_Build it. Question it. Understand it._
