#!/bin/bash
read -r -d '' VAR << EndOfMSG
<div class="container">
<div class="item">

<img style="width:300px" src="img/$1">
</div>
</div>
EndOfMSG

echo "$VAR"
