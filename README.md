# Switch_GitConfigs

Switch your git configs easily.

```
.
├── switch_users.py
├── user
│   ├── gitConfig
│   └── ssh
│       ├── authorized_keys
│       ├── id_ed25519
│       ├── id_ed25519.pub
│       ├── id_rsa
│       ├── id_rsa.pub
│       └── known_hosts
└── work
    ├── gitConfig
    └── ssh
        ├── authorized_keys
        ├── id_ed25519
        ├── id_ed25519.pub
        ├── id_rsa
        ├── id_rsa.pub
        └── known_hosts
```

### gitConfig file

```
user.email=email@email.com
user.name=XYZ
```
You can get this by doing
```bash
git config --list > gitConfig
```

### ssh folder

Copy contents from `~/.ssh` folder.
