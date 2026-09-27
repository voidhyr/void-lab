# void-lab

> Curious about how things work and what’s possible.
> Learning by building and experimenting.

## About

I'm Dani Sam (voidhyr), an aspiring software engineer building Python tools,
web scrapers and data projects. This lab documents my practice, experiments
and lessons learned.

I am still developing my Python and SQL skills and have some experience with
NumPy, Pandas and Matplotlib. I am also interested in Green AI, accessible
computing and independent experimentation.

Software development remains my foundation. I want to build useful tools,
understand them deeply and explore how computing can become more accessible
to people with limited resources. The applications may change as I learn.

## Currently Learning & Exploring

| Area | Current focus |
| --- | --- |
| Python development | Functions, modules, debugging, testing and reusable code |
| Data workflows | Scraping, cleaning, validation, SQL and SQLite |
| Maths & machine learning | Statistics, linear algebra and introductory ML |
| Green AI | Exploring resource-efficient and accessible AI |

These are learning directions, not claims of mastery or completed research.

## Learning Path

1. **Strengthen Python through projects.** Build small tools that I can explain,
   modify and debug independently.
2. **Make data workflows reliable.** Practise HTTP requests, parsing, validation,
   error handling and meaningful tests through the scraper project.
3. **Use SQL where it helps.** Start new small local applications with SQLite;
   learn joins, constraints, transactions and indexes through practical use.
4. **Study maths alongside code.** Explore statistics and linear algebra with
   small examples, NumPy calculations and plots.
5. **Learn basic machine learning.** Use scikit-learn, simple baselines and
   appropriate train, validation and test splits.
6. **Explore through experiments.** Ask clear questions, compare approaches
   and document what I learn.

These stages overlap. I do not need to master every topic before building.
Git, Linux, debugging and documentation are part of the process throughout.

FastAPI, Docker, PostgreSQL and Airflow are project-dependent tools rather than
prerequisites for every experiment. NoSQL is an option when the data and access
patterns justify it. Some experiments only need files and Pandas.

## Current Projects

### Books to Scrape — Learning Project

A Python scraper using HTTPX, BeautifulSoup and SQLite to collect book titles,
links, prices, ratings and availability from Books to Scrape.

The next milestone is a reliable small version: correct extraction, separate
parsing and execution, handle failures, test with local HTML samples and verify
duplicate-safe database updates. These are improvement goals, not a statement
that every item is already complete.

[Browse the scraper](fundamentals/scrapers/books_toscrape/)

### Weather ETL Pipeline

The separate **proETL** project provides practice with Python, SQL and data
quality. Its intended workflow collects OpenWeather data, validates records,
loads a PostgreSQL star schema and schedules processing with Apache Airflow.
Looker Studio is the planned reporting layer.

The project README is the source for its current implementation status. My use
of SQLite for new local tools does not require replacing PostgreSQL here.

[View proETL](https://github.com/voidhyr/proETL)

## Exploring

Interested in Green AI, accessible computing and independent experimentation.
My direction is evolving as I learn, build and test ideas.

## Repository Organisation

| Folder | Purpose |
| --- | --- |
| `fundamentals/basics/` | Introductory Python exercises and small scripts |
| `fundamentals/intermediate/` | Additional Python practice and small games |
| `fundamentals/intermediate-2/` | Collections, loops and other practice scripts |
| `fundamentals/oop/` | Object-oriented programming practice |
| `fundamentals/patterns/` | Pattern-printing exercises |
| `fundamentals/dsa/` | Searching, sorting, graph algorithms and other exercises |
| `fundamentals/scrapers/books_toscrape/` | Book scraper and SQLite storage |
| `archive/` | Earlier projects retained for reference |

Additional folders will be introduced when they contain actual work.

## Tools

- **Main language:** Python
- **Data and storage:** SQL, SQLite, NumPy, Pandas and Matplotlib
- **Development environment:** Ubuntu/Linux, PyCharm, uv and Git/GitHub
- **Scraping:** HTTPX and BeautifulSoup
- **Next learning tool:** scikit-learn
- **Project-dependent:** PostgreSQL, FastAPI, Docker and Apache Airflow

I use uv for Python environments and dependencies. Other environment managers
are optional when a specific project needs them.

## Working Principles

- Build small, useful programs before expanding their scope.
- Understand code well enough to explain, change and debug it.
- Use AI assistance thoughtfully; verify its output and document assistance where relevant.
- Prefer simple approaches when they solve the problem adequately.
- Write tests for meaningful behaviour, including failure cases.
- Respect source access rules and rate limits when collecting data.
- Document setup, limitations, results and lessons learned.
- Report unsuccessful experiments honestly and distinguish evidence from assumptions.

## Connect

[**Enter the Void → Personal Site**](https://voidhyr.github.io/Personal-Website/)

[Articles](https://dev.to/voidhyr) · [X](https://x.com/voidhyr)

_Build it. Question it. Understand it._
