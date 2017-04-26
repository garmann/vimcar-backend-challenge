CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL UNIQUE,
  `hash` varchar(150) NOT NULL,
  `status` int(5) NOT NULL DEFAULT 0,
  PRIMARY KEY (`email`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activationlink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(100) NOT NULL,
  `link` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`userid`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`userid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
