using System.Collections;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;
using UnityEngine.UIElements;


public class AlienSpawn : MonoBehaviour
{
    [SerializeField]
    private AlienSO alienSO;
    private GameObject Alien; // Randomly selected Alien

    [SerializeField]
    private float spawnRate;
    private float timer;

    public Transform spawnParent;
    private Transform[] createAlienLine;

    void Awake()
    {
        timer = 0;
        RandomSpawnState();
    }


    void Update()
    {
        if (timer < spawnRate)
        {
            timer += Time.deltaTime;
        }
        else
        {
            spawnAlien();
            timer = 0;
        }
    }

    void spawnAlien()
    {
        int randomIndex = Random.Range(0, createAlienLine.Length);
        if (randomIndex == 3) {
            randomIndex = 4;
        }
        Transform selectedSpawn = createAlienLine[randomIndex];

        Vector3 spawnPosition = selectedSpawn.position;
        spawnPosition.z -= 1;
        Quaternion spawnRotation = selectedSpawn.rotation;

        AlienType();
        Instantiate(Alien, spawnPosition, spawnRotation);
    }

    void AlienType()
    {
        int randomAlien = Random.Range(0, alienSO.alienItems.Length-1);
        if (randomAlien>=3) {
            randomAlien+= 1;
        }

        Alien = alienSO.alienItems[randomAlien].Prefab;
    }

    void RandomSpawnState()
    {
        createAlienLine = new Transform[transform.childCount];
        for (int i = 0; i < transform.childCount; i++)
        {
            createAlienLine[i] = transform.GetChild(i).transform;
        }
    }
}
