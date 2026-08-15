# Phishing URL Detonation Sandbox – SOC L1 Hands-on Lab

## Overview

This project is a hands-on SOC L1 security lab for safely analyzing suspicious URLs in an isolated Docker environment.

The sandbox uses Python, Playwright, and Chromium to automatically open a submitted URL, observe basic web behavior, collect HTTP and page information, capture a screenshot, and generate an investigation report.

The purpose of this project is to demonstrate practical phishing-analysis and evidence-collection skills relevant to a Security Operations Center (SOC).

---

## Objectives

- Safely analyze suspicious URLs without using a normal browser
- Execute browser activity inside a disposable Docker container
- Observe HTTP response information
- Identify the final destination URL
- Capture the rendered webpage as evidence
- Generate an investigation report
- Practice basic SOC investigation and documentation

---

## Architecture

```text
                 Suspicious URL
                       |
                       v
              +------------------+
              | Docker Container |
              +--------+---------+
                       |
                       v
                Python Script
                       |
                       v
              Playwright + Chromium
                       |
             +---------+---------+
             |         |         |
             v         v         v
         HTTP      Final URL   Page Title
         Status
             |         |         |
             +---------+---------+
                       |
                       v
                  Screenshot
                       |
                       v
                Investigation
                    Report


| Technology         | Purpose                           |
| ------------------ | --------------------------------- |
| Kali Linux         | Security analysis environment     |
| VMware Workstation | Virtualized lab environment       |
| Docker             | Container isolation               |
| Python             | Automation and analysis           |
| Playwright         | Browser automation                |
| Chromium           | Headless browser                  |
| Bash               | Command-line execution            |
| Git/GitHub         | Version control and documentation |


Lab Environment
Operating System: Kali Linux
Virtualization: VMware Workstation
Containerization: Docker
Browser: Chromium
Automation: Playwright
Network Mode: NAT

A VMware snapshot was created before setting up the lab to provide a rollback point.