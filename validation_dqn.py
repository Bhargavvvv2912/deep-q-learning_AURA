import sys
import os

def validate_dqn_environment():
    print("--- 🕹️ DQN Legacy Integrity Check ---")
    
    try:
        # 1. THE NAMESPACE TRAP: Standalone Keras
        # In modern stacks, 'import keras' might lead to Keras 3.0
        # which lacks the 'engine' or 'optimizers' structure of 2018.
        import keras
        from keras.models import Sequential
        from keras.layers import Dense
        from keras.optimizers import Adam
        print(f"SUCCESS: Legacy Keras {keras.__version__} engine found.")

        # 2. THE GYM REGISTRATION TRAP
        # Modern 'gym' (gymnasium) requires a 'render_mode' or has 
        # deprecated the 'v0' environments.
        import gym
        env = gym.make('CartPole-v0')
        state_size = env.observation_space.shape[0]
        print(f"SUCCESS: Gym 'CartPole-v0' initialized. State size: {state_size}")

        # 3. THE MODEL-GYM BRIDGE
        # Verify we can build a simple DQN model with the legacy API
        model = Sequential()
        model.add(Dense(24, input_dim=state_size, activation='relu'))
        model.add(Dense(2, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=0.001))
        print("SUCCESS: DQN Model compiled with Legacy API.")
        
        return True

    except Exception as e:
        print(f"\nCRITICAL: RL ENVIRONMENT DECAY!")
        print(f"Failure: {type(e).__name__} - {e}")
        return False

if __name__ == "__main__":
    if validate_dqn_environment():
        print("\n--- BASELINE GREEN ---")
        sys.exit(0)
    else:
        print("\n--- VALIDATION RED ---")
        sys.exit(1)