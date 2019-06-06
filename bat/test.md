# Host Scan

bat -h x.x.x.x/x

# Port Scan

bat -p x.x.x.x
bat -p x.x.x.x p
bat -p x.x.x.x/x p


bat -p syn/ack/... x.x.x.x
bat -p syn/ack/... x.x.x.x p
bat -p syn/ack/... x.x.x.x/x p

# Attack

## list scripts of bat

bat -a list

## Execute script

bat -a script-name
