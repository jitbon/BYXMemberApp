
DROP DATABASE IF EXISTS FratMembers;
CREATE DATABASE FratMembers;
USE frat_members;

DROP TABLE IF EXISTS members_info;
CREATE TABLE members_info(
	mID INT AUTO_INCREMENT,
    memberLName VARCHAR(100),
    memberFName VARCHAR(100),
    memberRole VARCHAR(60),
    memberClass CHAR(2),
    memberNum INT,
    PRIMARY KEY(mID)
) ENGINE=INNODB;
    