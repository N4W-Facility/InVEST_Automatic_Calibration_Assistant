# User Guide for the InVEST Calibration Assistant
The InVEST Calibration Assistant is a tool designed to help you efficiently calibrate hydrological and water quality models. Follow these steps to use it effectively:

## 1. Select the Model to Calibrate
InVEST offers several models, but the Calibration Assistant is only compatible with the following:
- Annual Water Yield (AWY)
- Seasonal Water Yield (SWY)
- Sediment Delivery Ratio (SDR)
- Nutrient Delivery Ratio (NDR)
Ensure the model you want to calibrate is on this list.

## 2. Set Up Your Project Structure
Before starting, organize your data as follows:
- Create a main folder containing all the biophysical information for your watershed. This information must be specific to the model you are calibrating.
- Refer to the “**UserData**” sheet in the configuration file. There, you’ll find a table indicating the required data for each model with an “**X**”
- For each model, create a specific folder using the following format:
     - Basin_Cal_[Model Name]
     - For example: Basin_Cal_AWY.
     - Inside this folder, save the shapefile of the watersheds you will use for calibration. Make sure the shapefile includes the “**ws_id**” field, which will be used to link observed data to the watersheds.

## 3. Input the Required Information
- In the “**UserData**” sheet, enter the file names (without extensions) and ensure they are in the specified units. Cells marked in red are the ones you need to modify.
- Below each model, you’ll find an option to select whether to calibrate it or not:
     - “**0**”: Do not calibrate the model.
     - “**1**”: Calibrate the model.
Set this to “**1**” for the models you want to calibrate.

## 4. Configure Parameter Search Ranges
- In the “**Params**” sheet, define the minimum and maximum values for the calibration parameters of each model.
- If you want to run a direct simulation without calibration, enter the desired value in the “**Value**” column.
- Once calibration is complete, the assistant will update the “**Value**” column with the calibrated values.

## 5. Input Observed Data
- In the “**Obs_Data**” sheet, enter the observed data for each calibration watershed.
- Ensure the “**ws_id**” matches the one in the watershed shapefiles.

## 6. General Recommendations
- **Coordinate system**: Use the same geographic projection for all raster and shapefile inputs.
- **Pixel size**: Choose a pixel size appropriate for the watershed size. For large watersheds, a 100-meter pixel may be a good option, but keep in mind that smaller pixels can significantly increase processing time.
- **Close the master file**: Before running the assistant, ensure the master file is closed to avoid errors.

## Additional Tips
- **Plan your calibration**: Calibration can be time-consuming, especially for large watersheds. Make sure you have enough time and computational resources.
- **Verify your data**: Before starting calibration, double-check that all data is complete and in the correct format.
- **Document your changes**: Save a copy of the original files before making modifications, so you can revert changes if needed.

By following these steps, you’ll be ready to use the InVEST Calibration Assistant efficiently. Good luck with your project!