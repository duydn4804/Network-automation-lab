# Network Automation & Security Provisioning Lab 🚀

## 📌 Project Overview
This project focuses on automating network management and enhancing security within a Cisco-based infrastructure. By integrating **Python** and **Ansible**, the lab moves away from manual CLI configurations to an **Infrastructure as Code (IaC)** approach, ensuring consistency, speed, and reduced human error.

## 🖼 Network Topology
![Topology](./Topology/Topology.png)

## ✨ Core Features
* **Automated Configuration:** Used **Ansible Playbooks** to deploy standardized routing and switching policies across multiple devices simultaneously.
* **Dynamic Security Enforcement:** Implemented **Time-Based ACLs** via Ansible (`block_time.yml`) to automatically restrict inter-network traffic based on scheduled business hours.
* **Automated Backups:** Developed a **Python script** (`backup_network.py`) to perform daily configuration backups, saving snapshots of each device to a centralized directory (`/backup_configs`).

## 🛠 Tech Stack
* **Automation:** Ansible, Python (Netmiko).
* **Infrastructure:** Cisco IOS.
* **Platform:** EVE-NG, Ubuntu Server.

## 📂 Project Structure
```text
├── Topology/           # Network diagram
│   └── Topology.png
├── ansible/            # Ansible automation files
│   ├── ansible.cfg     # Ansible configuration
│   ├── block_time.yml  # Playbook for Time-Based ACL deployment
│   └── hosts.ini       # Inventory file
├── backup_configs/     # Sample outputs of automated backups
├── python/             # Python scripts
│   └── backup_network.py
└── README.md           # Project documentation
