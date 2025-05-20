# trace generated using paraview version 5.13.0-RC2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
m000000vts = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
m000000vtsDisplay = GetDisplayProperties(m000000vts, view=renderView1)

# set scalar coloring
ColorBy(m000000vtsDisplay, ('POINTS', 'm', 'Z'))

# rescale color and/or opacity maps used to include current data range
m000000vtsDisplay.RescaleTransferFunctionToDataRange(True, False)

# get 2D transfer function for 'm'
mTF2D = GetTransferFunction2D('m')
mTF2D.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
mTF2D.Boxes = []
mTF2D.ScalarRangeInitialized = 0
mTF2D.Range = [0.0, 1.0, 0.0, 1.0]
mTF2D.OutputDimensions = [10, 10]

# get color transfer function/color map for 'm'
mLUT = GetColorTransferFunction('m')
mLUT.InterpretValuesAsCategories = 0
mLUT.AnnotationsInitialized = 0
mLUT.ShowCategoricalColorsinDataRangeOnly = 0
mLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
mLUT.RescaleOnVisibilityChange = 0
mLUT.TransferFunction2D = mTF2D
mLUT.RGBPoints = [-0.9999985098838806, 0.02, 0.3813, 0.9981, -0.9523796240488688, 0.02000006, 0.424267768, 0.96906969, -0.9047607382138569, 0.02, 0.467233763, 0.940033043, -0.8571418523788452, 0.02, 0.5102, 0.911, -0.8095229665438335, 0.02000006, 0.546401494, 0.872669438, -0.7619040807088215, 0.02, 0.582600362, 0.83433295, -0.7142851948738097, 0.02, 0.6188, 0.796, -0.6666663090387981, 0.02000006, 0.652535156, 0.749802434, -0.6190474232037864, 0.02, 0.686267004, 0.703599538, -0.5714285373687744, 0.02, 0.72, 0.6574, -0.5238096515337625, 0.02000006, 0.757035456, 0.603735359, -0.47619076569875074, 0.02, 0.794067037, 0.55006613, -0.428571879863739, 0.02, 0.8311, 0.4964, -0.3809529940287272, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, -0.33333410819371545, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, -0.2857152223587036, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, -0.2380963365236919, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, -0.19047745068868005, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, -0.1428585648536682, 0.6439, 0.9773, 0.0469, -0.09523967901865638, 0.762401813, 0.984669591, 0.034600153, -0.04762079318364465, 0.880901185, 0.992033407, 0.022299877, -1.9073486328125e-06, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 0.047616978486379136, 0.999402998, 0.955036376, 0.079066628, 0.09523586432139086, 0.9994, 0.910666223, 0.148134024, 0.1428547501564026, 0.9994, 0.8663, 0.2172, 0.19047363599141431, 0.999269665, 0.818035981, 0.217200652, 0.23809252182642626, 0.999133332, 0.769766184, 0.2172, 0.285711407661438, 0.999, 0.7215, 0.2172, 0.3333302934964497, 0.99913633, 0.673435546, 0.217200652, 0.38094917933146166, 0.999266668, 0.625366186, 0.2172, 0.4285680651664734, 0.9994, 0.5773, 0.2172, 0.47618695100148534, 0.999402998, 0.521068455, 0.217200652, 0.5238058368364968, 0.9994, 0.464832771, 0.2172, 0.5714247226715088, 0.9994, 0.4086, 0.2172, 0.6190436085065205, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 0.6666624943415325, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 0.7142813801765442, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 0.7619002660115559, 0.949903037, 0.116867171, 0.252900603, 0.8095191518465679, 0.903199533, 0.078432949, 0.291800389, 0.8571380376815796, 0.8565, 0.04, 0.3307, 0.9047569235165913, 0.798902627, 0.04333345, 0.358434298, 0.952375809351603, 0.741299424, 0.0466667, 0.386166944, 0.999994695186615, 0.6837, 0.05, 0.4139]
mLUT.UseLogScale = 0
mLUT.UseOpacityControlPointsFreehandDrawing = 0
mLUT.ShowDataHistogram = 0
mLUT.AutomaticDataHistogramComputation = 0
mLUT.DataHistogramNumberOfBins = 10
mLUT.ColorSpace = 'RGB'
mLUT.UseBelowRangeColor = 0
mLUT.BelowRangeColor = [0.0, 0.0, 0.0]
mLUT.UseAboveRangeColor = 0
mLUT.AboveRangeColor = [0.5, 0.5, 0.5]
mLUT.NanColor = [1.0, 0.0, 0.0]
mLUT.NanOpacity = 1.0
mLUT.Discretize = 1
mLUT.NumberOfTableValues = 256
mLUT.ScalarRangeInitialized = 1.0
mLUT.HSVWrap = 0
mLUT.VectorComponent = 2
mLUT.VectorMode = 'Component'
mLUT.AllowDuplicateScalars = 1
mLUT.Annotations = []
mLUT.ActiveAnnotatedValues = []
mLUT.IndexedColors = []
mLUT.IndexedOpacities = []
mLUT.EnableOpacityMapping = 0

# get opacity transfer function/opacity map for 'm'
mPWF = GetOpacityTransferFunction('m')
mPWF.Points = [-0.9999985098838806, 0.0, 0.5, 0.0, 0.999994695186615, 1.0, 0.5, 0.0]
mPWF.AllowDuplicateScalars = 1
mPWF.UseLogScale = 0
mPWF.ScalarRangeInitialized = 1
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219009e-08, 1.1005450535281953e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# set scalar coloring
ColorBy(m000000vtsDisplay, ('POINTS', 'm', 'Y'))

# rescale color and/or opacity maps used to exactly fit the current data range
m000000vtsDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(mLUT, m000000vtsDisplay)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219009e-08, 1.1005450535281953e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# set scalar coloring
ColorBy(m000000vtsDisplay, ('POINTS', 'm', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
m000000vtsDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(mLUT, m000000vtsDisplay)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219009e-08, 1.1005450535281953e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# Properties modified on m000000vts
m000000vts.TimeArray = 'None'

# show data in view
m000000vtsDisplay = Show(m000000vts, renderView1, 'StructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
m000000vtsDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# set scalar coloring
ColorBy(m000000vtsDisplay, ('POINTS', 'm', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
m000000vtsDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(mLUT, m000000vtsDisplay)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
mLUT.ApplyPreset('Rainbow Uniform', True)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
mLUT.ApplyPreset('Rainbow Uniform', True)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# create a new 'Glyph With Custom Source'
glyphWithCustomSource1 = GlyphWithCustomSource(registrationName='GlyphWithCustomSource1', Input=m000000vts,
    GlyphSource=None)
glyphWithCustomSource1.OrientationArray = ['POINTS', 'm']
glyphWithCustomSource1.ScaleArray = ['POINTS', 'No scale array']
glyphWithCustomSource1.VectorScaleMode = 'Scale by Magnitude'
glyphWithCustomSource1.ScaleFactor = 3.8199999607968493e-08
glyphWithCustomSource1.GlyphTransform = 'Transform2'
glyphWithCustomSource1.GlyphMode = 'Uniform Spatial Distribution'
glyphWithCustomSource1.MaximumNumberOfSamplePoints = 5000
glyphWithCustomSource1.Seed = 10339
glyphWithCustomSource1.Stride = 1

# init the 'Transform2' selected for 'GlyphTransform'
glyphWithCustomSource1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
glyphWithCustomSource1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
glyphWithCustomSource1.GlyphTransform.Scale = [1.0, 1.0, 1.0]
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07

# Properties modified on glyphWithCustomSource1
glyphWithCustomSource1.ScaleArray = ['POINTS', 'm']
glyphWithCustomSource1.VectorScaleMode = 'Scale by Components'
glyphWithCustomSource1.GlyphMode = 'Every Nth Point'
glyphWithCustomSource1.Stride = 10

# show data in view
glyphWithCustomSource1Display = Show(glyphWithCustomSource1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyphWithCustomSource1Display.Selection = None
glyphWithCustomSource1Display.Representation = 'Surface'
glyphWithCustomSource1Display.ColorArrayName = ['POINTS', 'm']
glyphWithCustomSource1Display.LookupTable = mLUT
glyphWithCustomSource1Display.MapScalars = 1
glyphWithCustomSource1Display.MultiComponentsMapping = 0
glyphWithCustomSource1Display.InterpolateScalarsBeforeMapping = 1
glyphWithCustomSource1Display.UseNanColorForMissingArrays = 0
glyphWithCustomSource1Display.Opacity = 1.0
glyphWithCustomSource1Display.PointSize = 2.0
glyphWithCustomSource1Display.LineWidth = 1.0
glyphWithCustomSource1Display.RenderLinesAsTubes = 0
glyphWithCustomSource1Display.RenderPointsAsSpheres = 0
glyphWithCustomSource1Display.DisableLighting = 0
glyphWithCustomSource1Display.Diffuse = 1.0
glyphWithCustomSource1Display.Interpolation = 'Gouraud'
glyphWithCustomSource1Display.Specular = 0.0
glyphWithCustomSource1Display.SpecularColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.SpecularPower = 100.0
glyphWithCustomSource1Display.Luminosity = 0.0
glyphWithCustomSource1Display.Ambient = 0.0
glyphWithCustomSource1Display.Roughness = 0.3
glyphWithCustomSource1Display.Metallic = 0.0
glyphWithCustomSource1Display.EdgeTint = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.Anisotropy = 0.0
glyphWithCustomSource1Display.AnisotropyRotation = 0.0
glyphWithCustomSource1Display.BaseIOR = 1.5
glyphWithCustomSource1Display.CoatStrength = 0.0
glyphWithCustomSource1Display.CoatIOR = 2.0
glyphWithCustomSource1Display.CoatRoughness = 0.0
glyphWithCustomSource1Display.CoatColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.SelectNormalArray = 'None'
glyphWithCustomSource1Display.SelectTangentArray = 'None'
glyphWithCustomSource1Display.ComputePointNormals = 0
glyphWithCustomSource1Display.Splitting = 1
glyphWithCustomSource1Display.FeatureAngle = 30.0
glyphWithCustomSource1Display.SelectTCoordArray = 'None'
glyphWithCustomSource1Display.Texture = None
glyphWithCustomSource1Display.RepeatTextures = 1
glyphWithCustomSource1Display.InterpolateTextures = 0
glyphWithCustomSource1Display.SeamlessU = 0
glyphWithCustomSource1Display.SeamlessV = 0
glyphWithCustomSource1Display.UseMipmapTextures = 0
glyphWithCustomSource1Display.ShowTexturesOnBackface = 1
glyphWithCustomSource1Display.BaseColorTexture = None
glyphWithCustomSource1Display.NormalTexture = None
glyphWithCustomSource1Display.NormalScale = 1.0
glyphWithCustomSource1Display.CoatNormalTexture = None
glyphWithCustomSource1Display.CoatNormalScale = 1.0
glyphWithCustomSource1Display.MaterialTexture = None
glyphWithCustomSource1Display.OcclusionStrength = 1.0
glyphWithCustomSource1Display.AnisotropyTexture = None
glyphWithCustomSource1Display.EmissiveTexture = None
glyphWithCustomSource1Display.EmissiveFactor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.TextureTransform = 'Transform2'
glyphWithCustomSource1Display.EdgeOpacity = 1.0
glyphWithCustomSource1Display.BackfaceRepresentation = 'Follow Frontface'
glyphWithCustomSource1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.BackfaceOpacity = 1.0
glyphWithCustomSource1Display.Translation = [0.0, 0.0, 0.0]
glyphWithCustomSource1Display.Scale = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.Orientation = [0.0, 0.0, 0.0]
glyphWithCustomSource1Display.Origin = [0.0, 0.0, 0.0]
glyphWithCustomSource1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
glyphWithCustomSource1Display.Pickable = 1
glyphWithCustomSource1Display.Triangulate = 0
glyphWithCustomSource1Display.UseShaderReplacements = 0
glyphWithCustomSource1Display.ShaderReplacements = ''
glyphWithCustomSource1Display.NonlinearSubdivisionLevel = 1
glyphWithCustomSource1Display.MatchBoundariesIgnoringCellOrder = 0
glyphWithCustomSource1Display.UseDataPartitions = 0
glyphWithCustomSource1Display.OSPRayUseScaleArray = 'All Approximate'
glyphWithCustomSource1Display.OSPRayScaleArray = 'm'
glyphWithCustomSource1Display.OSPRayScaleFunction = 'Piecewise Function'
glyphWithCustomSource1Display.OSPRayMaterial = 'None'
glyphWithCustomSource1Display.Assembly = ''
glyphWithCustomSource1Display.SelectedBlockSelectors = ['']
glyphWithCustomSource1Display.BlockSelectors = ['/']
glyphWithCustomSource1Display.BlockColors = []
glyphWithCustomSource1Display.BlockColorArrayNames = []
glyphWithCustomSource1Display.BlockLookupTables = []
glyphWithCustomSource1Display.BlockUseSeparateColorMaps = []
glyphWithCustomSource1Display.BlockMapScalars = []
glyphWithCustomSource1Display.BlockInterpolateScalarsBeforeMappings = []
glyphWithCustomSource1Display.BlockOpacities = []
glyphWithCustomSource1Display.BlockMapScalarsGUI = 1
glyphWithCustomSource1Display.BlockInterpolateScalarsBeforeMappingsGUI = 1
glyphWithCustomSource1Display.BlockOpacitiesGUI = 1.0
glyphWithCustomSource1Display.Orient = 0
glyphWithCustomSource1Display.OrientationMode = 'Direction'
glyphWithCustomSource1Display.SelectOrientationVectors = 'm'
glyphWithCustomSource1Display.Scaling = 0
glyphWithCustomSource1Display.ScaleMode = 'No Data Scaling Off'
glyphWithCustomSource1Display.ScaleFactor = 3.8199999607968493e-08
glyphWithCustomSource1Display.SelectScaleArray = 'None'
glyphWithCustomSource1Display.GlyphType = 'Arrow'
glyphWithCustomSource1Display.UseGlyphTable = 0
glyphWithCustomSource1Display.GlyphTableIndexArray = 'None'
glyphWithCustomSource1Display.UseCompositeGlyphTable = 0
glyphWithCustomSource1Display.UseGlyphCullingAndLOD = 0
glyphWithCustomSource1Display.LODValues = []
glyphWithCustomSource1Display.ColorByLODIndex = 0
glyphWithCustomSource1Display.GaussianRadius = 1.9099999803984245e-09
glyphWithCustomSource1Display.ShaderPreset = 'Sphere'
glyphWithCustomSource1Display.CustomTriangleScale = 3
glyphWithCustomSource1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
glyphWithCustomSource1Display.Emissive = 0
glyphWithCustomSource1Display.ScaleByArray = 0
glyphWithCustomSource1Display.SetScaleArray = ['POINTS', 'm']
glyphWithCustomSource1Display.ScaleArrayComponent = 'X'
glyphWithCustomSource1Display.UseScaleFunction = 1
glyphWithCustomSource1Display.ScaleTransferFunction = 'Piecewise Function'
glyphWithCustomSource1Display.OpacityByArray = 0
glyphWithCustomSource1Display.OpacityArray = ['POINTS', 'm']
glyphWithCustomSource1Display.OpacityArrayComponent = 'X'
glyphWithCustomSource1Display.OpacityTransferFunction = 'Piecewise Function'
glyphWithCustomSource1Display.DataAxesGrid = 'Grid Axes Representation'
glyphWithCustomSource1Display.SelectionCellLabelBold = 0
glyphWithCustomSource1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
glyphWithCustomSource1Display.SelectionCellLabelFontFamily = 'Arial'
glyphWithCustomSource1Display.SelectionCellLabelFontFile = ''
glyphWithCustomSource1Display.SelectionCellLabelFontSize = 18
glyphWithCustomSource1Display.SelectionCellLabelItalic = 0
glyphWithCustomSource1Display.SelectionCellLabelJustification = 'Left'
glyphWithCustomSource1Display.SelectionCellLabelOpacity = 1.0
glyphWithCustomSource1Display.SelectionCellLabelShadow = 0
glyphWithCustomSource1Display.SelectionPointLabelBold = 0
glyphWithCustomSource1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
glyphWithCustomSource1Display.SelectionPointLabelFontFamily = 'Arial'
glyphWithCustomSource1Display.SelectionPointLabelFontFile = ''
glyphWithCustomSource1Display.SelectionPointLabelFontSize = 18
glyphWithCustomSource1Display.SelectionPointLabelItalic = 0
glyphWithCustomSource1Display.SelectionPointLabelJustification = 'Left'
glyphWithCustomSource1Display.SelectionPointLabelOpacity = 1.0
glyphWithCustomSource1Display.SelectionPointLabelShadow = 0
glyphWithCustomSource1Display.PolarAxes = 'Polar Axes Representation'
glyphWithCustomSource1Display.SelectInputVectors = ['POINTS', 'm']
glyphWithCustomSource1Display.NumberOfSteps = 40
glyphWithCustomSource1Display.StepSize = 0.25
glyphWithCustomSource1Display.NormalizeVectors = 1
glyphWithCustomSource1Display.EnhancedLIC = 1
glyphWithCustomSource1Display.ColorMode = 'Blend'
glyphWithCustomSource1Display.LICIntensity = 0.8
glyphWithCustomSource1Display.MapModeBias = 0.0
glyphWithCustomSource1Display.EnhanceContrast = 'Off'
glyphWithCustomSource1Display.LowLICContrastEnhancementFactor = 0.0
glyphWithCustomSource1Display.HighLICContrastEnhancementFactor = 0.0
glyphWithCustomSource1Display.LowColorContrastEnhancementFactor = 0.0
glyphWithCustomSource1Display.HighColorContrastEnhancementFactor = 0.0
glyphWithCustomSource1Display.AntiAlias = 0
glyphWithCustomSource1Display.MaskOnSurface = 1
glyphWithCustomSource1Display.MaskThreshold = 0.0
glyphWithCustomSource1Display.MaskIntensity = 0.0
glyphWithCustomSource1Display.MaskColor = [0.5, 0.5, 0.5]
glyphWithCustomSource1Display.GenerateNoiseTexture = 0
glyphWithCustomSource1Display.NoiseType = 'Gaussian'
glyphWithCustomSource1Display.NoiseTextureSize = 128
glyphWithCustomSource1Display.NoiseGrainSize = 2
glyphWithCustomSource1Display.MinNoiseValue = 0.0
glyphWithCustomSource1Display.MaxNoiseValue = 0.8
glyphWithCustomSource1Display.NumberOfNoiseLevels = 1024
glyphWithCustomSource1Display.ImpulseNoiseProbability = 1.0
glyphWithCustomSource1Display.ImpulseNoiseBackgroundValue = 0.0
glyphWithCustomSource1Display.NoiseGeneratorSeed = 1
glyphWithCustomSource1Display.CompositeStrategy = 'AUTO'
glyphWithCustomSource1Display.UseLICForLOD = 0
glyphWithCustomSource1Display.WriteLog = ''

# init the 'Transform2' selected for 'TextureTransform'
glyphWithCustomSource1Display.TextureTransform.Translate = [0.0, 0.0, 0.0]
glyphWithCustomSource1Display.TextureTransform.Rotate = [0.0, 0.0, 0.0]
glyphWithCustomSource1Display.TextureTransform.Scale = [1.0, 1.0, 1.0]

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
glyphWithCustomSource1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
glyphWithCustomSource1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
glyphWithCustomSource1Display.GlyphType.TipResolution = 6
glyphWithCustomSource1Display.GlyphType.TipRadius = 0.1
glyphWithCustomSource1Display.GlyphType.TipLength = 0.35
glyphWithCustomSource1Display.GlyphType.ShaftResolution = 6
glyphWithCustomSource1Display.GlyphType.ShaftRadius = 0.03
glyphWithCustomSource1Display.GlyphType.Invert = 0

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
glyphWithCustomSource1Display.ScaleTransferFunction.Points = [-0.9999666810035706, 0.0, 0.5, 0.0, 0.9999364614486694, 1.0, 0.5, 0.0]
glyphWithCustomSource1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
glyphWithCustomSource1Display.OpacityTransferFunction.Points = [-0.9999666810035706, 0.0, 0.5, 0.0, 0.9999364614486694, 1.0, 0.5, 0.0]
glyphWithCustomSource1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
glyphWithCustomSource1Display.DataAxesGrid.XTitle = 'X Axis'
glyphWithCustomSource1Display.DataAxesGrid.YTitle = 'Y Axis'
glyphWithCustomSource1Display.DataAxesGrid.ZTitle = 'Z Axis'
glyphWithCustomSource1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
glyphWithCustomSource1Display.DataAxesGrid.XTitleFontFile = ''
glyphWithCustomSource1Display.DataAxesGrid.XTitleBold = 0
glyphWithCustomSource1Display.DataAxesGrid.XTitleItalic = 0
glyphWithCustomSource1Display.DataAxesGrid.XTitleFontSize = 12
glyphWithCustomSource1Display.DataAxesGrid.XTitleShadow = 0
glyphWithCustomSource1Display.DataAxesGrid.XTitleOpacity = 1.0
glyphWithCustomSource1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
glyphWithCustomSource1Display.DataAxesGrid.YTitleFontFile = ''
glyphWithCustomSource1Display.DataAxesGrid.YTitleBold = 0
glyphWithCustomSource1Display.DataAxesGrid.YTitleItalic = 0
glyphWithCustomSource1Display.DataAxesGrid.YTitleFontSize = 12
glyphWithCustomSource1Display.DataAxesGrid.YTitleShadow = 0
glyphWithCustomSource1Display.DataAxesGrid.YTitleOpacity = 1.0
glyphWithCustomSource1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
glyphWithCustomSource1Display.DataAxesGrid.ZTitleFontFile = ''
glyphWithCustomSource1Display.DataAxesGrid.ZTitleBold = 0
glyphWithCustomSource1Display.DataAxesGrid.ZTitleItalic = 0
glyphWithCustomSource1Display.DataAxesGrid.ZTitleFontSize = 12
glyphWithCustomSource1Display.DataAxesGrid.ZTitleShadow = 0
glyphWithCustomSource1Display.DataAxesGrid.ZTitleOpacity = 1.0
glyphWithCustomSource1Display.DataAxesGrid.FacesToRender = 63
glyphWithCustomSource1Display.DataAxesGrid.CullBackface = 0
glyphWithCustomSource1Display.DataAxesGrid.CullFrontface = 1
glyphWithCustomSource1Display.DataAxesGrid.ShowGrid = 0
glyphWithCustomSource1Display.DataAxesGrid.ShowEdges = 1
glyphWithCustomSource1Display.DataAxesGrid.ShowTicks = 1
glyphWithCustomSource1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
glyphWithCustomSource1Display.DataAxesGrid.AxesToLabel = 63
glyphWithCustomSource1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
glyphWithCustomSource1Display.DataAxesGrid.XLabelFontFile = ''
glyphWithCustomSource1Display.DataAxesGrid.XLabelBold = 0
glyphWithCustomSource1Display.DataAxesGrid.XLabelItalic = 0
glyphWithCustomSource1Display.DataAxesGrid.XLabelFontSize = 12
glyphWithCustomSource1Display.DataAxesGrid.XLabelShadow = 0
glyphWithCustomSource1Display.DataAxesGrid.XLabelOpacity = 1.0
glyphWithCustomSource1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
glyphWithCustomSource1Display.DataAxesGrid.YLabelFontFile = ''
glyphWithCustomSource1Display.DataAxesGrid.YLabelBold = 0
glyphWithCustomSource1Display.DataAxesGrid.YLabelItalic = 0
glyphWithCustomSource1Display.DataAxesGrid.YLabelFontSize = 12
glyphWithCustomSource1Display.DataAxesGrid.YLabelShadow = 0
glyphWithCustomSource1Display.DataAxesGrid.YLabelOpacity = 1.0
glyphWithCustomSource1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
glyphWithCustomSource1Display.DataAxesGrid.ZLabelFontFile = ''
glyphWithCustomSource1Display.DataAxesGrid.ZLabelBold = 0
glyphWithCustomSource1Display.DataAxesGrid.ZLabelItalic = 0
glyphWithCustomSource1Display.DataAxesGrid.ZLabelFontSize = 12
glyphWithCustomSource1Display.DataAxesGrid.ZLabelShadow = 0
glyphWithCustomSource1Display.DataAxesGrid.ZLabelOpacity = 1.0
glyphWithCustomSource1Display.DataAxesGrid.XAxisNotation = 'Mixed'
glyphWithCustomSource1Display.DataAxesGrid.XAxisPrecision = 2
glyphWithCustomSource1Display.DataAxesGrid.XAxisUseCustomLabels = 0
glyphWithCustomSource1Display.DataAxesGrid.XAxisLabels = []
glyphWithCustomSource1Display.DataAxesGrid.YAxisNotation = 'Mixed'
glyphWithCustomSource1Display.DataAxesGrid.YAxisPrecision = 2
glyphWithCustomSource1Display.DataAxesGrid.YAxisUseCustomLabels = 0
glyphWithCustomSource1Display.DataAxesGrid.YAxisLabels = []
glyphWithCustomSource1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
glyphWithCustomSource1Display.DataAxesGrid.ZAxisPrecision = 2
glyphWithCustomSource1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
glyphWithCustomSource1Display.DataAxesGrid.ZAxisLabels = []
glyphWithCustomSource1Display.DataAxesGrid.UseCustomBounds = 0
glyphWithCustomSource1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
glyphWithCustomSource1Display.PolarAxes.Visibility = 0
glyphWithCustomSource1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
glyphWithCustomSource1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
glyphWithCustomSource1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
glyphWithCustomSource1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.EnableCustomRange = 0
glyphWithCustomSource1Display.PolarAxes.CustomRange = [0.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.AutoPole = 1
glyphWithCustomSource1Display.PolarAxes.PolarAxisVisibility = 1
glyphWithCustomSource1Display.PolarAxes.RadialAxesVisibility = 1
glyphWithCustomSource1Display.PolarAxes.DrawRadialGridlines = 1
glyphWithCustomSource1Display.PolarAxes.PolarArcsVisibility = 1
glyphWithCustomSource1Display.PolarAxes.DrawPolarArcsGridlines = 1
glyphWithCustomSource1Display.PolarAxes.NumberOfRadialAxes = 0
glyphWithCustomSource1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
glyphWithCustomSource1Display.PolarAxes.NumberOfPolarAxes = 5
glyphWithCustomSource1Display.PolarAxes.DeltaRangePolarAxes = 0.0
glyphWithCustomSource1Display.PolarAxes.CustomMinRadius = 1
glyphWithCustomSource1Display.PolarAxes.MinimumRadius = 0.0
glyphWithCustomSource1Display.PolarAxes.CustomMaxRadius = 0
glyphWithCustomSource1Display.PolarAxes.MaximumRadius = 1.0
glyphWithCustomSource1Display.PolarAxes.CustomAngles = 1
glyphWithCustomSource1Display.PolarAxes.MinimumAngle = 0.0
glyphWithCustomSource1Display.PolarAxes.MaximumAngle = 90.0
glyphWithCustomSource1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
glyphWithCustomSource1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
glyphWithCustomSource1Display.PolarAxes.Ratio = 1.0
glyphWithCustomSource1Display.PolarAxes.EnableOverallColor = 1
glyphWithCustomSource1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleVisibility = 1
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
glyphWithCustomSource1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
glyphWithCustomSource1Display.PolarAxes.PolarLabelVisibility = 1
glyphWithCustomSource1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
glyphWithCustomSource1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
glyphWithCustomSource1Display.PolarAxes.PolarLabelOffset = 10.0
glyphWithCustomSource1Display.PolarAxes.PolarExponentOffset = 5.0
glyphWithCustomSource1Display.PolarAxes.RadialTitleVisibility = 1
glyphWithCustomSource1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
glyphWithCustomSource1Display.PolarAxes.RadialTitleLocation = 'Bottom'
glyphWithCustomSource1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
glyphWithCustomSource1Display.PolarAxes.RadialUnitsVisibility = 1
glyphWithCustomSource1Display.PolarAxes.ScreenSize = 10.0
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleBold = 0
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleItalic = 0
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleShadow = 0
glyphWithCustomSource1Display.PolarAxes.PolarAxisTitleFontSize = 12
glyphWithCustomSource1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
glyphWithCustomSource1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
glyphWithCustomSource1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyphWithCustomSource1Display.PolarAxes.PolarAxisLabelBold = 0
glyphWithCustomSource1Display.PolarAxes.PolarAxisLabelItalic = 0
glyphWithCustomSource1Display.PolarAxes.PolarAxisLabelShadow = 0
glyphWithCustomSource1Display.PolarAxes.PolarAxisLabelFontSize = 12
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTextBold = 0
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTextItalic = 0
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTextShadow = 0
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTextFontSize = 12
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
glyphWithCustomSource1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
glyphWithCustomSource1Display.PolarAxes.EnableDistanceLOD = 1
glyphWithCustomSource1Display.PolarAxes.DistanceLODThreshold = 0.7
glyphWithCustomSource1Display.PolarAxes.EnableViewAngleLOD = 1
glyphWithCustomSource1Display.PolarAxes.ViewAngleLODThreshold = 0.7
glyphWithCustomSource1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
glyphWithCustomSource1Display.PolarAxes.PolarTicksVisibility = 1
glyphWithCustomSource1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
glyphWithCustomSource1Display.PolarAxes.TickLocation = 'Both'
glyphWithCustomSource1Display.PolarAxes.AxisTickVisibility = 1
glyphWithCustomSource1Display.PolarAxes.AxisMinorTickVisibility = 0
glyphWithCustomSource1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
glyphWithCustomSource1Display.PolarAxes.DeltaRangeMajor = 1.0
glyphWithCustomSource1Display.PolarAxes.DeltaRangeMinor = 0.5
glyphWithCustomSource1Display.PolarAxes.ArcTickVisibility = 1
glyphWithCustomSource1Display.PolarAxes.ArcMinorTickVisibility = 0
glyphWithCustomSource1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
glyphWithCustomSource1Display.PolarAxes.DeltaAngleMajor = 10.0
glyphWithCustomSource1Display.PolarAxes.DeltaAngleMinor = 5.0
glyphWithCustomSource1Display.PolarAxes.TickRatioRadiusSize = 0.02
glyphWithCustomSource1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
glyphWithCustomSource1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
glyphWithCustomSource1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
glyphWithCustomSource1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
glyphWithCustomSource1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
glyphWithCustomSource1Display.PolarAxes.ArcMajorTickSize = 0.0
glyphWithCustomSource1Display.PolarAxes.ArcTickRatioSize = 0.3
glyphWithCustomSource1Display.PolarAxes.ArcMajorTickThickness = 1.0
glyphWithCustomSource1Display.PolarAxes.ArcTickRatioThickness = 0.5
glyphWithCustomSource1Display.PolarAxes.Use2DMode = 0
glyphWithCustomSource1Display.PolarAxes.UseLogAxis = 0

# show color bar/color legend
glyphWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329095e-07, -7.412660108219004e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.245677113650065e-07, -2.8112893796548027e-08, 9.204752511378349e-07]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.1874190987882098e-07, 9.914963464313145e-09, 7.71657232633405e-07]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.2456771136500647e-07, -2.8112893796548027e-08, 9.204752511378349e-07]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.3161693116329092e-07, -7.412660108219009e-08, 1.100545053528195e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.4014648711921513e-07, -1.2980318689781694e-07, 1.3184295144205312e-06]
renderView1.CameraFocalPoint = [1.9099999803984247e-07, 1.9099999803984247e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.022763174874592344, 0.968402957448156, 0.2483496524565595]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [2.462150857227761e-07, -4.5136847407636946e-07, 1.18805438367377e-06]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984244e-07, 6.30000016599297e-08]
renderView1.CameraViewUp = [-0.011895470703859705, 0.8681029719627277, 0.49624160229288844]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.986385448978095e-07, -3.5442816499644743e-07, 1.1665271904720995e-06]
renderView1.CameraFocalPoint = [1.909999980398425e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5265359330983361, 0.6686803057709292, 0.5250014855506232]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.278913590794846e-07, -2.597670788496531e-07, 9.75005942827012e-07]
renderView1.CameraFocalPoint = [1.909999980398425e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5265359330983361, 0.6686803057709292, 0.5250014855506232]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1612, 749)

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07

# save animation
SaveAnimation(filename='C:/Users/User/Downloads/mumax3.10_windows_cuda9.2/x_1/ok.mp4', viewOrLayout=renderView1, location=16, ImageResolution=[1612, 748],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=1,
    FrameStride=1,
    FrameWindow=[0, 4], 
    # MP4 Writer options
    FileName='',
    BitRate=10000000)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1612, 749)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [5.657213985713013e-07, -2.8753987650491774e-07, 9.456239555208742e-07]
renderView1.CameraFocalPoint = [1.9099999803984244e-07, 1.9099999803984276e-07, 6.300000165992951e-08]
renderView1.CameraViewUp = [-0.5097179937499702, 0.6469326460416239, 0.567155814863154]
renderView1.CameraParallelScale = 2.773643789522923e-07


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------