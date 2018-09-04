### Abstract

The California Department of Transportation (Caltrans) faces a challenge to address the large amount of trash being littered by commercial and personal vehicles traveling on its highways. Trash on the highway is often washed into drainage facilities (e.g. inlets and culverts) during rain storms, which drain to water bodies. As a result, it impacts water quality statewide and is regulated as a pollutant of concern$^{1}$ by the State Water Resource Control Board (SWRCB).

This study outlines the data, methods and results used for developing a strategy to address the trash problem on California highways. Specifically, it seeks to answer the following questions regarding trash control:

1. What are the key factors influencing trash collection volume?
2. Can we accurately predict trash collection volume based on these key factors?
3. Do trash collection efficiency rates vary between highways with different trash levels?

Prior to starting the study, trash collection volume was assumed to be influenced by labor and efficiency rates would vary due to different trash generation levels and roadway geometry.

### Introduction

In addition to being a pollution source, trash is a safety hazard when accumulated in large amounts. As a result, current Caltrans trash collection efforts as follows:

1. Routine trash pickup and roadside sweeping.
2. Adopt-A-Highway Program$^{2}$, Department of Corrections and Rehabilitation trash pickup and organized volunteer events.
3. Protect Every Drop$^{3}$ public education campaign consisting of media advertising, public outreach events and organized trash pickup events.
4. Integration of trash capture devices into new highway projects and incorporating trash capture into project planning and development practices$^{4}$.
5. Policy development to prioritize trash collection efforts.

### Statewide Trash Amendments and San Francisco (SF) Bay Region Requirements

Many cities and municipalities face similar trash issues on their roads, sidewalks and parking areas where trash is littered, accumulated and washed into drainage facilities during rain storms. As a result, the SWRCB has issued adopted its Trash Amendments under the National Pollutant Discharge Elimination System (NPDES) permit effective June 1, 2017. Caltrans is required to achieve compliance with these requirements and demonstrate progress towards milestones within the amendment$^{5}$.

In addition, Caltrans is required to achieve compliance with the San Francisco Bay Region requirements of the current Caltrans NPDES permit$^{6}$. Specifically, it is required to demonstrate progress towards achieving the schedule and milestones for achieving full-trash capture as required by the region-specific requirements. Trash capture can be achieved by integrating structural controls such as trash screening devices into drainage facilities. In areas where such controls are not possible, then Caltrans is considering alternatives for meeting full-trash capture equivalency with enhanced trash collection efforts.

Caltrans is currently addressing the San Francisco Bay Region (Attachment V) requirements of the Caltrans NPDES permit which have more immediate compliance deadlines than the statewide requirements; as a result, the SF Bay Area effort is being develop prior to the statewide effort. However, similar data analysis will be used to develop compliance benchmarks for both efforts. Since the SF Bay Area effort is separate from the statewide effort, it was excluded from the scope of this study.

### Statewide Trash Control Strategy

Achieving compliance with the statewide Trash Provisions and SF Bay Region requirements will require significant resources; as a result, Caltrans is developing its strategy as follows:

1. Identify Trash Generating Level: Analyze trash collection data to identify trash generating levels for all corridors and baseline level of trash collection effort.
2. Complete On-Land Visual Trash Assessments (OVTAs): Verify trash generating levels for corridors and segments with conflicting trash level scores.
3. Develop Trash Assessment Model: Modify analytical model developed for the SF Bay region-specific requirements to develop compliance benchmarks for the statewide Trash Amendments.

### Data Analysis for Decision Making

Alternative methods of data collection such as field monitoring and inspections are cost prohibitive. As a result, data analysis is the most time and cost effective method for decision making for developing a strategy to achieve compliance with regulatory requirements$^{7}$.

### Trash Generation and Discharge

This study focuses on trash collection rates but does not attempt to measure trash generation and discharge rates, which will be needed to evaluate current and future levels of effort in trash collection. In general, the relationship between these values can be expressed as follows:

**Trash Generated - Trash Collected = Trash Left on Ground Surfaces + Trash Discharged**

As a result, trash volume and sweeping are only one component of this relationship and help identify where and how to focus trash collection efforts. However, trash generation rates and quantity left of ground surfaces will be worth additional study to measure compliance with full-trash capture requirements of the trash amendment.

### Trash Collection Data

Trash collection data was analyzed which consisted of approximately 100,000 total records dating from 2012 through 2017. The results from analyzing the population data are more robust due to the larger sample size. The trash collection data was extracted from a work order tracking system for logging all trash cleanup activities completed by Caltrans. As a result, the dataset contains various units of measure; however, only trash volume (cubic yard) was considered in this study.

### Tools and Process

The tools and process listed below were used to create the data model for this study:

1. Jupyter Notebook - Exploratory data analysis, visualization and regression models were completed using Python within this notebook.
2. Azure ML (AML) - Feature importance was evaluated and predictive models developed using AML
3. Python Modules - The modules listed below were used for this study and will need to be installed in order to run this notebook:

  * Pandas
  * NumPy
  * SciPy
  * Seaborn
  * Matplotlib
  * StatsModels
  * Scikit-Learn
