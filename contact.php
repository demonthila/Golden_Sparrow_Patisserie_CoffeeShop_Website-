<?php
// Golden Sparrow Patisserie – contact form handler (Hostinger PHP mail)
$to = 'admin@goldensparrowpatisserie.com.au';

function back($status) { header('Location: contact.html?' . $status . '#top'); exit; }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') back('');
if (!empty($_POST['website'])) back('sent=1');            // honeypot: silently drop bots

$clean = function ($v, $max) { $v = trim((string)($v ?? '')); $v = str_replace(["\r", "\n"], ' ', $v); return mb_substr($v, 0, $max); };
$name    = $clean($_POST['name'] ?? '', 100);
$email   = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$phone   = $clean($_POST['phone'] ?? '', 40);
$topic   = $clean($_POST['topic'] ?? 'General enquiry', 60);
$date    = $clean($_POST['date'] ?? '', 20);
$message = mb_substr(trim((string)($_POST['message'] ?? '')), 0, 5000);

if ($name === '' || !$email || $message === '') back('error=1');

$host = preg_replace('/[^a-z0-9.\-]/i', '', $_SERVER['HTTP_HOST'] ?? 'goldensparrowpatisserie.com.au');
$subject = "Website enquiry: $topic – $name";
$body  = "New enquiry from the Golden Sparrow Patisserie website\n\n";
$body .= "Name: $name\nEmail: $email\nPhone: " . ($phone ?: '-') . "\nTopic: $topic\nDate needed: " . ($date ?: '-') . "\n\nMessage:\n$message\n";
$headers  = "From: Golden Sparrow Website <noreply@$host>\r\n";
$headers .= "Reply-To: $name <$email>\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

back(@mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers) ? 'sent=1' : 'error=1');
