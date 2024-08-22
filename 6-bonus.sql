--sql project
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
BEGIN
	DECLARE project_id INTEGER;

	INSERT INTO projects(name)
	SELECT project_name FROM DUAL
	WHERE NOT EXISTS(SELECT 1 FROM projects WHERE name = project_name LIMIT 1);

	SELECT id INTO project_id
	FROM projects
	WHERE name = project_name;


	INSERT INTO corrections(user_id, project_id, score)
	VALUES (user_id, project_id, score);

END $$
DELIMITER ;
