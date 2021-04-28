def reactiveStageBoundary(currentNstage):
    middleStage = round(currentNstage/2)
    lb = [middleStage, currentNstage -1]
    up = [2, middleStage + 1]
    return lb, ub


def funcAspen(x, *agrs):

    currentNstage, refluxRatioVector[indexRefluxRatio], feedStageVector[indexFeedStage] = args
    reactiveStage1, reactiveStage2 = x

    #Star ASPEN simulation
    aspen.Reinit()

    #Args value
    #Number of stage in column
    Application.Tree.FindNode("\Data\Blocks\CR\Input\NSTAGE").Value = currentNstage
    #Number of feed stage of oxygen 
    Application.Tree.FindNode("\Data\Blocks\CR\Input\FEED_STAGE\OXY").Value = currentNstage - 1
    #Number of reflux ratio
    Application.Tree.FindNode("\Data\Blocks\CR\Input\BASIS_RR").Value = refluxRatioVector
    #Numeber of feed stage of glycerin
    Application.Tree.FindNode("\Data\Blocks\CR\Input\FEED_STAGE\FEED").Value = feedStageVector

    #Variable value
    Application.Tree.FindNode("\Data\Blocks\CR\Input\REAC_STAGE1\#0").Value = reactiveStage1
    Application.Tree.FindNode("\Data\Blocks\CR\Input\REAC_STAGE2\#0").Value = reactiveStage2

    #Run simulation
    aspen.Engine.Run2()

    reboilerHeatDuty = Application.Tree.FindNode("\Data\Blocks\CR\Output\REB_DUTY").Value
    aspen.Close()

    return reboilerHeatDuty