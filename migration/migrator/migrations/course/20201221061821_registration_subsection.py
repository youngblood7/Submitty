"""Migration for a given Submitty course database."""


def up(config, database, semester, course):
    database.execute("ALTER TABLE ONLY users ALTER COLUMN registration_subsection SET DATA TYPE character varying(255) USING registration_subsection::varchar(255)")



def down(config, database, semester, course):
    database.execute("ALTER TABLE ONLY users ALTER COLUMN registration_subsection SET DATA TYPE integer USING registration_subsection::integer")
