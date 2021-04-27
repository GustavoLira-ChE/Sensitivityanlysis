def funcAspen(currentNstage, refluxRatioVector[indexRefluxRatio], feedStageVector[indexFeedStage]:
    aspen.Reinit()
    #Number of stage in column
    Application.Tree.FindNode("\Data\Blocks\CR\Input\NSTAGE").Value = currentNstage
    #Number of feed stage of oxygen 
    Application.Tree.FindNode("\Data\Blocks\CR\Input\FEED_STAGE\OXY").Value = currentNstage - 1
    #Number of reflux ratio
    Application.Tree.FindNode("\Data\Blocks\CR\Input\BASIS_RR").Value = refluxRatioVector
    #Numeber of feed stage of glycerin
    Application.Tree.FindNode("\Data\Blocks\CR\Input\FEED_STAGE\FEED").Value = feedStageVector

    