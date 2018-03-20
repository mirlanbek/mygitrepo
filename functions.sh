#!/bin/bash


restart_network (){

systemctl daemon-reload
systemctl restart network


}


restart_ypbind (){

systemctl daemon-reload
systemctl restart ypbind
systemctl enable ypbind

}

test1 (){

echo "this is from test function"

}



