Implemented Models: DCGAN, GAN, WGAN, CGAN, WGAN_GP

## Config File Details.

+ "model_choice" : Choosing particular GAN model. e.g. "WGAN", "DCGAN", "GAN"
+ "save_dir": Specifying the local directory path to save generated images during different epoch of training. e.g. "Results/WGAN"
+ "sample_interval": Interval within an epoch for saving results of generated images with currently trained model. Default Value is 400
+ "GAN_model" (Parameters for training the model)
  + "epochs": Number of epochs to run the training process for.
  + "mini_batch_size": Size of the mini-batch. 
  + "clip_value": Value for clipping the loss. Used in models such as WGAN. To use clipping during training simply specify a non-negative value. To not use clipping the vlaue for the variable set is negative. Default value is -1.
  + "n_critic": Value of critic to update Generator weights. Used in WGAN. To use critic based updates during trainig the model simply specify a non-negative number. To not use critic the vlaue for the variable set is negative. Default value is -1.

+ "genetative_network" (Parameters for the generator network)
  + "input_shape": Input size of the image. e.g. For a 28*28 image the values is 28.
  + "latent_dim": Parameter for setting the latent dimension.
  + "channels": Number of color channels in the image. e.g. 3 for RGB. 1 for Black and White.
  + "optimizer" (Parameters for the optimizer)
    + "learning_rate": Learning rate.
    + "b1" and "b2": Coefficients used for computing running averages of gradient and its square. Used in Adam optimizer.
    
+ "discriminator_network" (Parameters for the discriminator network)
  + "input_shape": Input size of the image. e.g. For a 28*28 image the values is 28.
  + "latent_dim": Parameter for setting the latent dimension.
  + "channels": Number of color channels in the image. e.g. 3 for RGB. 1 for Black and White.
  + "optimizer" (Parameters for the optimizer)
    + "learning_rate": Learning rate.
    + "b1" and "b2": Coefficients used for computing running averages of gradient and its square. Used in Adam optimizer.

## Configure the config.json file

+ Choose Model
+ Choose Parameter Values
+ Define Path to input file
+ Define Path to output file

```json
{
    "model_choice":"WGAN",
    
    "save_dir":"Results/WGAN",

    "sample_interval":"200",

    "data_path":"Datasets/dataset1.p",

    "data_label":"1",

    "GAN_model":{
        "epochs":"1",
        "mini_batch_size":"",
        "clip_value":"",
        "n_critic":"",
        "lambda_gp":""
    },

    "genetative_network":{
        "input_shape":"",
        "latent_dim":"",
        "channels":"",
        "optimizer":{
            "learning_rate":"",
            "b1":"",
            "b2":""
        }
    },
    
    "discriminator_network":{
        "input_shape":"",
        "channels":"",
        "optimizer":{
            "learning_rate":"",
            "b1":"",
            "b2":""
        }
    }
}
```