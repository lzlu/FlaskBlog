/*
Navicat MySQL Data Transfer

Source Server         : aliyun
Source Server Version : 50161
Source Host           : rdsm3amreurv2ae.mysql.rds.aliyuncs.com:3306
Source Database       : rpvea7nkuothm1c9

Target Server Type    : MYSQL
Target Server Version : 50161
File Encoding         : 65001

Date: 2015-11-05 17:18:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('21802f8b016');

-- ----------------------------
-- Table structure for imgdir
-- ----------------------------
DROP TABLE IF EXISTS `imgdir`;
CREATE TABLE `imgdir` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_dir` varchar(200) DEFAULT NULL,
  `add_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_imgdir_add_time` (`add_time`),
  KEY `ix_imgdir_img_dir` (`img_dir`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of imgdir
-- ----------------------------

-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text,
  `timestamp` datetime DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `title` varchar(64) DEFAULT NULL,
  `body_html` text,
  `last_modified` datetime DEFAULT NULL,
  `body_slug` text,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `ix_posts_timestamp` (`timestamp`),
  KEY `ix_posts_title` (`title`),
  KEY `ix_posts_last_modified` (`last_modified`),
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=392 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of posts
-- ----------------------------
INSERT INTO `posts` VALUES ('386', '##关于本博客\r\n\r\n  开始写日志了，手有点抖，这个blog（勉强称得上系统），是我为毕设做准备用flask搭的。主要参考（抄）Flask Web Development  [戳这](http://book.douban.com/subject/25814739/)，从中学到了很多，也算勉强开发出来一个blog来，想看源码 [戳这](https://github.com/Expelliarmus923/FlaskBlog)，欢迎拍砖。\r\n\r\n从数据库到jiaji2模板，在到服务器的Gunicorn+Supervisor+Nginx全部溜了一遍，对web开发流程也更熟悉了，为接下来毕设网上商城的设计打好基础。\r\n\r\n\r\n', '2015-09-28 15:56:37', '2', '第0篇日志', '<h2>关于本博客</h2>\n<p>开始写日志了，手有点抖，这个blog（勉强称得上系统），是我为毕设做准备用flask搭的。主要参考（抄）Flask Web Development  <a href=\"http://book.douban.com/subject/25814739/\" rel=\"nofollow\">戳这</a>，从中学到了很多，也算勉强开发出来一个blog来，想看源码 <a href=\"https://github.com/Expelliarmus923/FlaskBlog\" rel=\"nofollow\">戳这</a>，欢迎拍砖。</p>\n<p>从数据库到jiaji2模板，在到服务器的Gunicorn+Supervisor+Nginx全部溜了一遍，对web开发流程也更熟悉了，为接下来毕设网上商城的设计打好基础。</p>', '2015-10-21 15:36:14', '<h2>关于本博客</h2>\n<p>开始写日志了，手有点抖，这个blog（勉强称得上系统），是我为毕设做准备用flask搭的。主要参考（抄）Flask Web Development  <a href=\"http://book.douban.com/subject/25814739/\" rel=\"nofollow\">戳这</a>，从中学到了很多，也算勉强开发出来一个blog来，想看源码 <a href=\"https://github.com/Expelliarmus923/FlaskBlog\" rel=\"nofollow\">戳这</a>，欢迎拍砖。</p>\n<p>从数据库到jiaji2模板，在到服务器的Gunicorn+Supervisor+Nginx全部溜了一遍，对web开发流程也更熟悉了，为接下来毕设网上商城的设计打好基础。</p>');
INSERT INTO `posts` VALUES ('389', '##给岁月以文明，给时光以生命\r\n\r\n>《呼兰河传》\r\n\r\n>《三体I》\r\n\r\n> 《三体II》\r\n\r\n>《解忧杂货铺》', '2015-10-27 09:17:03', '2', '已完成的书单', '<h2>给岁月以文明，给时光以生命</h2>\n<blockquote>\n<p>《呼兰河传》</p>\n<p>《三体I》</p>\n<p>《三体II》</p>\n<p>《解忧杂货铺》</p>\n</blockquote>', '2015-10-28 10:37:44', '<h2>给岁月以文明，给时光以生命</h2>\n<blockquote>\n<p>《呼兰河传》</p>\n<p>《三体I》</p>\n<p>《三体II》</p>\n<p>《解忧杂货铺》</p>\n</blockquote>');
INSERT INTO `posts` VALUES ('390', '##计划之前\r\n\r\n有幸在知乎上拜读了萧井博大大神的文章  [编程入门指南](http://zhuanlan.zhihu.com/xiao-jing-mo/19959253) ,开始思考编程到底是什么，以及评估自己现状。\r\n\r\n首先也是最重要的一点，我真的不懂编程到底是什么，这是个很根本的原因，对于学习的影响很大，我甚至不知道自己到底喜不喜欢编程。所以搞懂这点是十分重要的。\r\n<!--more-->\r\n***\r\n##计划一\r\n下面是萧大提供的是启蒙的学习计划\r\n> 视频\r\n\r\n>> [哈佛大学公开课：计算机科学cs50](http://v.163.com/special/opencourse/cs50.html)\r\n\r\n>>[ 计算机科学和Python编程导论](http://www.xuetangx.com/courses/course-v1:MITx+6_00_1x+2015_T2/about)\r\n\r\n> 书籍\r\n\r\n>>[编码的奥秘](http://book.douban.com/subject/1024570/)\r\n\r\n>>[C语言编程](http://book.douban.com/subject/1786294/)\r\n\r\n预计一个月(2015-11-28完成)\r\n', '2015-10-28 10:33:05', '2', '不迷惘，从头学', '<h2>计划之前</h2>\n<p>有幸在知乎上拜读了萧井博大大神的文章  <a href=\"http://zhuanlan.zhihu.com/xiao-jing-mo/19959253\" rel=\"nofollow\">编程入门指南</a> ,开始思考编程到底是什么，以及评估自己现状。</p>\n<p>首先也是最重要的一点，我真的不懂编程到底是什么，这是个很根本的原因，对于学习的影响很大，我甚至不知道自己到底喜不喜欢编程。所以搞懂这点是十分重要的。\n</p>\n\n<h2>计划一</h2>\n<p>下面是萧大提供的是启蒙的学习计划</p>\n<blockquote>\n<p>视频</p>\n<blockquote>\n<p><a href=\"http://v.163.com/special/opencourse/cs50.html\" rel=\"nofollow\">哈佛大学公开课：计算机科学cs50</a></p>\n<p><a href=\"http://www.xuetangx.com/courses/course-v1:MITx+6_00_1x+2015_T2/about\" rel=\"nofollow\"> 计算机科学和Python编程导论</a></p>\n</blockquote>\n<p>书籍</p>\n<blockquote>\n<p><a href=\"http://book.douban.com/subject/1024570/\" rel=\"nofollow\">编码的奥秘</a></p>\n<p><a href=\"http://book.douban.com/subject/1786294/\" rel=\"nofollow\">C语言编程</a></p>\n</blockquote>\n</blockquote>\n<p>预计一个月(2015-11-28完成)</p>', '2015-10-28 10:35:11', '<h2>计划之前</h2>\n<p>有幸在知乎上拜读了萧井博大大神的文章  <a href=\"http://zhuanlan.zhihu.com/xiao-jing-mo/19959253\" rel=\"nofollow\">编程入门指南</a> ,开始思考编程到底是什么，以及评估自己现状。</p>\n<p>首先也是最重要的一点，我真的不懂编程到底是什么，这是个很根本的原因，对于学习的影响很大，我甚至不知道自己到底喜不喜欢编程。所以搞懂这点是十分重要的。</p>');
INSERT INTO `posts` VALUES ('391', '##接下来要做的事\r\n\r\n>1.用前端用angularjs构建一个todo-list，后台Flask保存数据，完成用户注册登录。\r\n\r\n>2.Javascript写一个PinJs的插件，具体效果就是在图片上指定位置添加Text。后台NodeJs处理保存图片位置信息。\r\n', '2015-11-03 00:58:37', '2', '接下来', '<h2>接下来要做的事</h2>\n<blockquote>\n<p>1.用前端用angularjs构建一个todo-list，后台Flask保存数据，完成用户注册登录。</p>\n<p>2.Javascript写一个PinJs的插件，具体效果就是在图片上指定位置添加Text。后台NodeJs处理保存图片位置信息。</p>\n</blockquote>', '2015-11-03 00:58:37', '<h2>接下来要做的事</h2>\n<blockquote>\n<p>1.用前端用angularjs构建一个todo-list，后台Flask保存数据，完成用户注册登录。</p>\n<p>2.Javascript写一个PinJs的插件，具体效果就是在图片上指定位置添加Text。后台NodeJs处理保存图片位置信息。</p>\n</blockquote>');

-- ----------------------------
-- Table structure for post_tages
-- ----------------------------
DROP TABLE IF EXISTS `post_tages`;
CREATE TABLE `post_tages` (
  `Post_id` int(11) DEFAULT NULL,
  `Tage_id` int(11) DEFAULT NULL,
  KEY `Post_id` (`Post_id`),
  KEY `Tage_id` (`Tage_id`),
  CONSTRAINT `post_tages_ibfk_1` FOREIGN KEY (`Post_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `post_tages_ibfk_2` FOREIGN KEY (`Tage_id`) REFERENCES `tags` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post_tages
-- ----------------------------
INSERT INTO `post_tages` VALUES ('386', '47');
INSERT INTO `post_tages` VALUES ('389', '49');
INSERT INTO `post_tages` VALUES ('390', '51');
INSERT INTO `post_tages` VALUES ('390', '52');
INSERT INTO `post_tages` VALUES ('391', '53');

-- ----------------------------
-- Table structure for roles
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_roles_default` (`default`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES ('4', 'Administrator', '0', '255');
INSERT INTO `roles` VALUES ('5', 'Moderator', '0', '7');
INSERT INTO `roles` VALUES ('6', 'User', '1', '7');

-- ----------------------------
-- Table structure for tags
-- ----------------------------
DROP TABLE IF EXISTS `tags`;
CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(64) DEFAULT NULL,
  `tag_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_tags_tag_name` (`tag_name`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tags
-- ----------------------------
INSERT INTO `tags` VALUES ('47', '日志', '1');
INSERT INTO `tags` VALUES ('48', '学习', '0');
INSERT INTO `tags` VALUES ('49', '书单', '1');
INSERT INTO `tags` VALUES ('50', '编程;coder', '0');
INSERT INTO `tags` VALUES ('51', 'coder', '1');
INSERT INTO `tags` VALUES ('52', '编程', '1');
INSERT INTO `tags` VALUES ('53', '接下来', '1');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('2', 'admin', '1002359548@qq.com', '4', 'pbkdf2:sha1:1000$IfUz5r2C$b2ce539fb8acfc2e1815d8b84d1897c65269c471');
INSERT INTO `users` VALUES ('3', 'lulizhou', 'lulizhou@lulizhou.com', '6', 'pbkdf2:sha1:1000$77jZ35xL$52629fa9b26487f6e0778b17215653845517a236');
