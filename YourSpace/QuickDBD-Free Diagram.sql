-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/NsWn9V
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE `USER` (
    `ID` int  NOT NULL ,
    `userName` varchar  NOT NULL ,
    `name` varchar  NOT NULL ,
    `slug` slug  NOT NULL ,
    `description` textfield  NOT NULL ,
    `page_cover` img  NOT NULL ,
    `page_avatar` img  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `ProfileContent` (
    `ID` int  NOT NULL ,
    `Profile` varchar  NOT NULL ,
    `name` string  NOT NULL ,
    `type` string  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `TextContent` (
    `ID` int  NOT NULL ,
    `Name` varchar  NOT NULL ,
    `Content` textfield  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

CREATE TABLE `ImgContent` (
    `ID` int  NOT NULL ,
    `Name` varchar  NOT NULL ,
    `Content` image  NOT NULL ,
    `profile` varchar  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);

ALTER TABLE `ProfileContent` ADD CONSTRAINT `fk_ProfileContent_Profile` FOREIGN KEY(`Profile`)
REFERENCES `USER` (`userName`);

ALTER TABLE `ImgContent` ADD CONSTRAINT `fk_ImgContent_profile` FOREIGN KEY(`profile`)
REFERENCES `USER` (`userName`);

