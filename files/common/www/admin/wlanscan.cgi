#!/bin/sh

export TITLE="Infos: WLAN-Scan"

. $DOCUMENT_ROOT/page-pre.sh ${0%/*}

cat<<EOM
<H2>$TITLE</H2>
<br>
<fieldset class="bubble">
<legend>Access Points (Automatische Aktualisierung)</legend>
<div id="ajax_wlan">
EOM

/www/cgi-bin/ajax-wlan.cgi no-html-header

cat<<EOM
</div>
</fieldset>
<SCRIPT LANGUAGE="JavaScript" TYPE="text/javascript"><!--
ajax_wlan();
//--></SCRIPT>

EOM

. $DOCUMENT_ROOT/page-post.sh ${0%/*}
