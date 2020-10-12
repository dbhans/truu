SELECT `admincomments`.* FROM `admincomments`;
SELECT `availability`.* FROM `availability`;
SELECT `classroom`.* FROM `classroom`;
SELECT `classroom_has_softwares`.* FROM `classroom_has_softwares`;
SELECT `cours`.* FROM `cours`;
SELECT `group`.* FROM `group`;
SELECT `logs`.* FROM `logs`;
SELECT `personnels`.* FROM `personnels`;
SELECT `programs`.* FROM `programs`;
SELECT `schedule`.* FROM `schedule`;
SELECT `semesters`.* FROM `semesters`;
SELECT `softwares`.* FROM `softwares`;
SELECT `teacherpreferences`.* FROM `teacherpreferences`;
SELECT `time`.* FROM `time`;

------rechercher les diponibilite
SELECT `personnels`.`idPersonnel`, `availability`.*
FROM `personnels` 
	LEFT JOIN `availability` ON `availability`.`Personnel_idPersonnel` = `personnels`.`idPersonnel`;
--- rechercher les preferencres por un professeur------- 
SELECT `cours`.*, `teacherpreferences`.*, `personnels`.*
FROM `cours` 
LEFT JOIN `teacherpreferences` ON `teacherpreferences`.`Cours_idCours` = `cours`.`idCours` 
LEFT JOIN `personnels` ON `teacherpreferences`.`Personnels_idPersonnel` = `personnels`.`idPersonnel`;

---recherche teachers time conflict cours
SSELECT `schedule`.*, `time`.`startTime`
FROM `schedule` 
	LEFT JOIN `time` ON `schedule`.`Time_idTime` = `time`.`idTime`
WHERE  XXXX BETWEEN (`time`.`startTime`,`time`.`endTime`);