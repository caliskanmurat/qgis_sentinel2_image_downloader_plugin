# QGIS Sentinel-2 Image Downloader Plugin

With this plugin, it is possible to download Sentinel-2 images (_B01, B02, B03, B04, B05, B06, B07, B08, B8A, B09, B10, B11, B12, TCI, SCL_) from the **_Copernicus Data Space Platform_** (https://dataspace.copernicus.eu/).
<br/>
<br/>
### Download Footprints
<img width="800" src="./images/image1.PNG">
<i>Download Footprints</i> section is first part of the analysis. In this section a <i><b>Geopackage (GPKG)</b></i> file is created. This file contains informations about the images to be downloaded such as "<i>prod_id, prod_identifier, prod_download_url, cloudcover, processingdate, area_km</i>". Images that are not desired to be downloaded should be deleted from the attribute table of the GPKG file.

<br/><br/>

<b>Query Area:</b> The extent of area of interest is selected here. Multiple options are available for to select _Query Area_:<br/>
- <ins>_Canvas Extent_</ins> : Extent of current canvas is used for query,
- <ins> _Drawing Manually From the Map_</ins> : Extent of query area is drawed manually,
- <ins> _Layer Extent_</ins> : Extent of layer is used for query. If **_Use features of layer for query_** option is selected, features of the selected layer is used for query. _Polygon, Point, Polyline_ data are available.

<br/><br/>

<b>Parameters:</b> Parameters for the images to be downloaded are specified here. The parameters are <i>maximum cloud coverage(%)</i>, <i>pruduct type (L2A, L1C, Both)</i> and <i>date range</i>.

<br/><br/>

<b>Output Folder:</b> Folder where the footprint files will be created in is specified here.

<br/><br/>

<img width="800" src="./images/image2.PNG">
<i>Download Images</i> section is second part of the analysis. In this section, the images in the attribute table of the GKPG file are downloaded.(<i>Copernicus Data Space account is required.</i>)<br/><br/>
<b>Go to Site for Registration:</b> This is a link to Copernicus Data Space platform for registration.<br/><br/>
<b>Input Footprint File:</b> Geopackage file that was created in first section is specified here.<br/><br/>
<b>Extract Files:</b> Sentinel images are downloaded in .zip format. So it has to be extracted before use. This option allows user to extract files after being downloaded automatically.<br/><br/>
<b>Delete Zip File:</b> This option should be selected if .zip file is desired to be deleted after process. This option is available if "<i>Extract files</i>" option is selected.<br/><br/>
<b>NDVI and NDWI:</b> This option should be selected if "<i>NDVI</i>" and "<i>NDWI</i>" indices are desired to be created after process. This option is available if "<i>Extract files</i>" option is selected. (NDVI and NDWI images are multiplied by 100 and images are saved in integer type to decrease the size.)<br/><br/>
<b>Clip by Extent as VRT:</b> If this option is selected, downloaded images are also clipped using specified extent beside original one. However, clipped image is saved in <i>Virtual Format(.VRT)</i> format not real one. This option is available if "<i>Extract files</i>" option is selected.<br/><br/>
<b>Download only quicklook file:</b> A quicklook file is small sized RGB image in .jpg format. It is not georeferenced and can be used for previewing and determining the images to be downloaded. This option can be selected to download only quicklook images before the Sentinel image bands.
<br/>
<br/>

<img width="800" src="./images/image3.PNG">
<i>Download Footprints</i> section is first part of the analysis. In this section a <i><b>Geopackage (GPKG)</b></i> file is created. This file contains informations about the images to be downloaded such as "prod_id, prod_identifier, prod_download_url, cloudcover, processingdate, area_km". Images that are not desired to be downloaded should be deleted from the attribute table of the GPKG file.<br/><br/>
<b>Query Area:</b> The extent of area of interest is selected here. It can be specified by "<i>Canvas Extent</i>", "<i>Layer Extent</i>" or "<i>Drawing Manually From the Map</i>".<br/><br/>
<b>Parameters:</b> Parameters for the images to be downloaded are specified here. The parameters are <i>maximum cloud coverage(%)</i>, <i>pruduct type (L2A, L1C, Both)</i> and <i>date range</i>.<br/><br/>
<b>Output Folder:</b> Folder where the footprint files will be created in is specified here.<br/><br/>
