queue()
	.defer(d3.json, piechartDataUrl)
    .await(ready);