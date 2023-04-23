<?php
// 获取表单提交的数据
$username = $_POST['username'];
$password = $_POST['password'];

// 打开文件
$file = fopen("user_info.txt", "a");

// 将数据写入文件
fwrite($file, $username . "," . $password . "\n");

// 关闭文件
fclose($file);

// 提示保存成功
echo "用户信息保存成功！每天6点自动执行打卡";
?>
