
def up(config, database, semester, course):
    database.execute("ALTER TABLE ONLY users ALTER COLUMN registration_subsection SET DATA TYPE character varying(255) USING registration_subsection::varchar(255)")
