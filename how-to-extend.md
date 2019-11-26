# Extending the code pattern

Pull requests and contribution are always welcome. To make this a more complete solution,
this application can be expanded in a couple of ways:

  * Contribute additional generator or discriminator components from different state-of-the-art GAN
  * Novel GAN leanring methods including reinforcement learning based learning or using meta-learning

Steps to extend this code pattern:

1. Set "custom" in model_choice in the config.json file.
2. Set path to the data file in the config file.
3. Set the values for network parameter. Check [Config File Details](https://github.ibm.com/DARVIZ/gan-toolkit-code-patterns/wiki/Documentation:-Config-File-Details) for details on possible value for each parameter.
4. Call network_parameter() function to read the parameter values form the config file.
```python 
network_parameters()
```
5. Import the generator network and discriminator network of your choice.
```python
from models.generator.generator6 import Generator
from models.discriminator.discriminator6 import Discriminator
```
Import the loss for the generator and discriminator of your choice.
```python
from models.loss.loss2 import loss_block as g_loss_block
from models.loss.loss2 import loss_block as d_loss_block
```
Import the optimizer for the generator and discriminator of your choice.
```python
from models.optimizer.optimizer1 import optimizer_block as g_optimizer_block
from models.optimizer.optimizer1 import optimizer_block as d_optimizer_block
```

After creating the custom function, run the following command:

```
python main.py --config <path_to_config_file>
``` 