#!/bin/sh
# v4.3 full rebuild in order (design generators). Usage: sh run_all.sh
set -e
cd "$(dirname "$0")"
python3 home43.py
python3 src43.py
python3 home_states.py
python3 orders43.py
python3 settings43.py
for g in pages_money pages_orders pages_queue pages_settings pages_books43; do python3 $g.py; done
for g in pages_control pages_sales pages_sell7 pages_delivery pages_offline pages_debts pages_buy7 pages_money7 pages_stock pages_products pages_period pages_books7 pages_setup pages_readiness pages_program pages_partners pages_connect pages_connect2 pages_connect3 pages_connect3b pages_connect4 pages_connect5; do python3 $g.py; done
python3 onboard43.py
python3 onboard_features.py
python3 onboard_flow.py
python3 firstsale.py
python3 onboard_aside.py
python3 relink.py
python3 status7.py
python3 nav7.py
python3 brand.py
python3 quiet_icons.py
python3 inert.py
python3 tracks7.py
python3 facts7.py
python3 links7.py
python3 offline7.py
python3 role7.py
python3 nav7.py
rm -rf __pycache__
