clear all;close all;clc;
path=[268    575;
         143    488;
         236    320;
         240   58;
         186   52];
y=imread("Color_Y.jpg");
initiallocation=path(1,:);
initialorientatin=pi;
robotgoal=path(end,:);
robotcurrentpose=[initiallocation initialorientatin]';
distancetogoal=norm(initiallocation-robotgoal);
radiusgoal=0.1;
controller=controllerPurePursuit;
controller.Waypoints=path;
controller.DesiredLinearVelocity=36;
controller.MaxAngularVelocity=18;
controller.LookaheadDistance=0.789;
robot=differentialDriveKinematics("TrackWidth",30,"VehicleInputs","VehicleSpeedHeadingRate");
sempaltime=0.1;
vizrate=rateControl(1/sempaltime);
framesize=robot.TrackWidth/0.8;
while(distancetogoal>radiusgoal)
    if (norm(robotcurrentpose(1:2)-controller.Waypoints(1,1))<90)
        controller.LookaheadDistance=2;
    elseif (norm(robotcurrentpose(1:2)-controller.Waypoints(1,1))<40)
        controller.LookaheadDistance=1;
    elseif (norm(robotcurrentpose(1:2)-controller.Waypoints(1,1))<20)
        controller.LookaheadDistance=0.5;
    end
    [v,omega]=controller(robotcurrentpose);
    val=derivative(robot,robotcurrentpose,[v,omega]);
    robotcurrentpose=robotcurrentpose+val*sempaltime;
    distancetogoal=norm(robotcurrentpose(1:2)-robotgoal(:));
    hold off
    imshow(y);
    hold on
    plot(path(:,1),path(:,2),"k--d");
    hold all
    plotTrVec=[robotcurrentpose(1:2);0];
    plotRot=axang2quat([0 0 1 robotcurrentpose(3)]);
    plotTransforms(plotTrVec',plotRot,"FrameSize",framesize,"MeshFilePath","groundvehicle.stl","View","2D");
    light;
    waitfor(vizrate);
end