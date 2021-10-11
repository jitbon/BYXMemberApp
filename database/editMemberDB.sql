USE FratMembers;

DROP PROCEDURE IF EXISTS addMember;

DELIMITER //

CREATE PROCEDURE addMember(IN lName VARCHAR(100),IN fName VARCHAR(100), IN role VARCHAR(60), IN class CHAR(2), IN num INT)
BEGIN

	INSERT INTO members_info (memberLName, memberFName, memberRole, memberClass, memberNum)
    VALUES (name, role, class, num);

END//

DELIMITER ;

-- ----------------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS deleteMember;

DELIMITER //

CREATE PROCEDURE deleteMember(IN lName VARCHAR(100), IN fName VARCHAR(100))
BEGIN 

	DELETE FROM members_info
    WHERE memberLName = lName AND memberFName = fName;
    
END//

DELIMITER ;

-- ----------------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS findMember;

DELIMITER //

CREATE PROCEDURE findMember(IN lName VARCHAR(100), IN fName VARCHAR(100))
BEGIN

	SELECT *
    FROM members_info
    WHERE memberLName = lName AND memberFName = fName;
    
END//

DELIMITER ;

-- ----------------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS editMemberNum;

DELIMITER //

CREATE PROCEDURE editMemberNum(IN ID INT, IN num INT)
BEGIN

	UPDATE members_info
    SET memberNum = num
    WHERE mID = ID;
    
END//

DELIMITER ;

-- ----------------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS editMemberClass;

DELIMITER //

CREATE PROCEDURE editMemberClass(IN ID INT, IN class CHAR(2))
BEGIN

	UPDATE members_info
    SET memberClass = class
    WHERE mID = ID;
    
END//

DELIMITER ;

-- ----------------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS editMemberRole;

DELIMITER //

CREATE PROCEDURE editMemberRole(IN ID INT, IN role VARCHAR(60))
BEGIN

	UPDATE members_info
    SET memberRole = role
    WHERE mID = ID;
    
END//

DELIMITER ;

-- ----------------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS editMemberFName;

DELIMITER //

CREATE PROCEDURE editMemberFName(IN ID INT, IN fName VARCHAR(100))
BEGIN

	UPDATE members_info
    SET memberFName = fName
    WHERE mID = ID;
    
END//

DELIMITER ;

-- ----------------------------------------------------------------------------------
DROP PROCEDURE IF EXISTS editMemberLName;

DELIMITER //

CREATE PROCEDURE editMemberLName(IN ID INT, IN lName VARCHAR(100))
BEGIN

	UPDATE members_info
    SET memberLName = lName
    WHERE mID = ID;
    
END//

DELIMITER ;