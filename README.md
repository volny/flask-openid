- Make the scripts executable `chmod a+x <script>.py`

- Run the devserver `./run.py`

- Create the db `./create_db.py`
- Migrate the db `./migrate_db.py`

- If you need to record a new migration `./upgrade_db.py`
- If you need to downgrade the db to an old format `./downgrade_db.py`

the `tmp/` folder is for flask-openID files. When moving to OAuth it can be deleted.
