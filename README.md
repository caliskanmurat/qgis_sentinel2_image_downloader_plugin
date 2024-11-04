# QGIS Sentinel-2 Image Downloader Plugin

With this plugin, it is possible to download Sentinel-2 images (_B01, B02, B03, B04, B05, B06, B07, B08, B8A, B09, B10, B11, B12, TCI, SCL_) from the **_Copernicus Data Space Platform_** (https://dataspace.copernicus.eu/). The process consists of two steps : "_Download Footprints_" and "_Download Images_".

<br/><br/>

### 1-) Download Footprints

<img width="800" src="./images/image1.PNG">
<i>Download Footprints</i> section is first part of the analysis. In this section a <i><b>Geopackage (GPKG)</b></i> file is created. This file contains informations about the images to be downloaded such as "<i>prod_id, prod_identifier, prod_download_url, cloudcover, processingdate, area_km</i>". Images that are not desired to be downloaded should be deleted from the attribute table of the GPKG file.

<br/><br/>

<b>Query Area:</b> The extent of area of interest is selected here. Multiple options are available to select _Query Area_:<br/>
- <ins>_Canvas Extent_</ins> : Extent of current canvas is used for query,
- <ins> _Drawing Manually From the Map_</ins> : Extent of query area is drawned manually on the canvas,
- <ins> _Layer Extent_</ins> : Extent of selected layer is used for query. If **_Use features of layer for query_** option is selected, features of the selected layer is used for query. This option is only available for _vector_ files. _Polygon, Point, Polyline_ data are available.

<br/>

<b>Parameters:</b> Parameters for the images to be downloaded are specified here. The parameters are <i>maximum cloud coverage(%)</i>, <i>pruduct type (L2A, L1C, Both)</i> and <i>date range</i>.

<br/>

<b>Output Folder:</b> Folder for files to be downloaded is specified here.

<br/><br/>

### 2-) Download Images

<img width="800" src="./images/image2.PNG">
<i>Download Images</i> section is second part of the analysis. In this section, the images in the attribute table of the GKPG files are downloaded.(<i>Copernicus Data Space account is required.</i>)

<br/><br/>

<b>Go to Site for Registration:</b> This is a link to _Copernicus Data Space_ platform for registration.

<br/>

<b>Input Footprint File(s):</b> Geopackage(GPKG) file(s) created in first section is specified here. Multiple files can be selected. 

<br/>

<b>Output Folder:</b> Folder for files to be downloaded is specified here.

<br/>

<b>OPTIONS:</b> Some extra options about download process can be configured in his section. Detailed explanation is below.

<br/>

<b>Download List:</b> The summary about process can be found here.

<br/><br/>

### Download Options

<img width="800" src="./images/image3.PNG">

<b>Bands:</b> Bands to be download can be selected here.

<br/>

<b>Indices:</b> Remote sensing indices that is desired to be created after download can be selected here.

<br/>

<b>Clip and Merge:</b> Downloaded images can be merged as VRT file based on _date, zone number and product type_ (e.g. merged_vrt\20241102\z35\MSIL2A). Also images can be clipped using query extent.

<br/>

<b>Other:</b> Beside downloading individual bands, _raw zip file_ and _quicklook file of the image_ also can be download by selecting this option.
