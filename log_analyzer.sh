#!/bin/bash

echo "=====LOGIN ACTIVITY REPORT ====="
echo ""

echo "Failed login attempts:"
grep "Failed password" /var/log/auth.log | wc -l

echo ""
echo "Success logins:"
grep "Accepted password" /var/log/auth.log | wc -l

echo ""
echo "Top IP addresses attempting login:"
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | head

echo ""
echo "Report generated on:"
date
